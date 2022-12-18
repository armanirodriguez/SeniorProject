from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponse
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from search.forms import SearchForm
from music.models import Song
from users.models import Profile
import users
from .forms import PostForm, CommentForm, createCommunityForm
from .models import Community, Post
import spotipy

def home(request):
    communityForm = createCommunityForm(request.POST)
    try:
        if(request.user.is_authenticated):
            user_profile = request.user.profile
        else:
            user_profile = ""
    except Profile.DoesNotExist:
        user_profile = Profile(user=request.user)
    users = Profile.objects.all()
    songs = None
    if request.method == "POST":
        if 'post_flag' in request.POST:
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.poster = request.user
                post.save()
                add_songs = list(filter(None, request.POST['songs_input'].split(',')))
                sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='616f55f94a904037a1eb6bdfbfa96d95', client_secret='2e262cfa37904ebeb74d43ff6903c9de'))
                if(add_songs):
                    for song in add_songs:
                        try:
                            newsong = Song(song_id = song)
                            song_name = sp.track(song).get('name')
                            newsong.song_name = song_name
                            newsong.save()
                        except:
                            print("song already in library")
                        tempsong = get_object_or_404(Song, song_id = song)
                        post.songs.add(tempsong)
                post.save()
                return HttpResponseRedirect(request.path_info)
        if 'search_flag' in request.POST:
            searchForm = SearchForm(request.POST)
            if searchForm.is_valid():
                query = searchForm.cleaned_data['query']
                songs = search_songs(query)
    posts = Post.objects.all().order_by('-timestamp')
    try:
        test = user_profile.joined_communities.all()
        posts = Post.objects.all().filter(community__in=test).order_by('-timestamp')
    except:
        posts = None
    
    # TODO: add community form to this
    return render(request, 'communityhome.html', {
        'form' : PostForm(),
        'posts' : posts,
        'communities' : Community.objects.all(),
        'searchForm': SearchForm(),
        'songs': songs,
        'user_profile': user_profile,
        'users': users,
        'comment_form': CommentForm(),
        'createCommunityForm': communityForm
    })
    
def homeVote(request):
    communityForm = createCommunityForm(request.POST)
    try:
        if(request.user.is_authenticated):
            user_profile = request.user.profile
        else:
            user_profile = ""
    except Profile.DoesNotExist:
        user_profile = Profile(user=request.user)
    users = Profile.objects.all()
    songs = None
    if request.method == "POST":
        if 'post_flag' in request.POST:
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.poster = request.user
                post.save()
                add_songs = list(filter(None, request.POST['songs_input'].split(',')))
                sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='616f55f94a904037a1eb6bdfbfa96d95', client_secret='2e262cfa37904ebeb74d43ff6903c9de'))
                if(add_songs):
                    for song in add_songs:
                        try:
                            newsong = Song(song_id = song)
                            song_name = sp.track(song).get('name')
                            newsong.song_name = song_name
                            newsong.save()
                        except:
                            print("song already in library")
                        tempsong = get_object_or_404(Song, song_id = song)
                        post.songs.add(tempsong)
                post.save()
                return HttpResponseRedirect(request.path_info)
        if 'search_flag' in request.POST:
            searchForm = SearchForm(request.POST)
            if searchForm.is_valid():
                query = searchForm.cleaned_data['query']
                songs = search_songs(query)
    posts = Post.objects.all().order_by('-timestamp')
    try:
        test = user_profile.joined_communities.all()
        posts = Post.objects.all().filter(community__in=test).order_by('-score')
    except:
        posts = None
    
    # TODO: add community form to this
    return render(request, 'communityhome.html', {
        'form' : PostForm(),
        'posts' : posts,
        'communities' : Community.objects.all(),
        'searchForm': SearchForm(),
        'songs': songs,
        'user_profile': user_profile,
        'users': users,
        'comment_form': CommentForm(),
        'createCommunityForm': communityForm
    })

def search_songs(query):
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='616f55f94a904037a1eb6bdfbfa96d95', client_secret='2e262cfa37904ebeb74d43ff6903c9de'))
    result = sp.search(q=query, type="track", limit=4)['tracks']['items']
    tracks = [item['id'] for item in result]
    return tracks

def community(request, community_name):
    communityForm = createCommunityForm(request.POST)
    songs = ""
    try:
        if(request.user.is_authenticated):
            user_profile = request.user.profile
        else:
            user_profile = ""
        community = Community.objects.get(name=community_name)
        comm_users = Profile.objects.filter(joined_communities__in=[community.id]).values()
    except Community.DoesNotExist:
        raise Http404('Community not found')
    if request.method == "POST":
        if 'post_flag' in request.POST:
                form = PostForm(request.POST)
                if form.is_valid():
                    post = form.save(commit=False)
                    post.poster = request.user
                    add_songs = list(filter(None, request.POST['songs_input'].split(',')))
                    post.save()
                    print(add_songs)
                    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='616f55f94a904037a1eb6bdfbfa96d95', client_secret='2e262cfa37904ebeb74d43ff6903c9de'))
                    if(add_songs):
                        for song in add_songs:
                            try:
                                newsong = Song(song_id = song)
                                song_name = sp.track(song).get('name')
                                newsong.song_name = song_name
                                newsong.save()
                            except:
                                print("song already in library")
                            tempsong = get_object_or_404(Song, song_id = song)
                            post.songs.add(tempsong)
                    post.save()
                    return HttpResponseRedirect(request.path_info)
        if 'search_flag' in request.POST:
                searchForm = SearchForm(request.POST)
                if searchForm.is_valid():
                    query = searchForm.cleaned_data['query']
                    songs = search_songs(query)
    posts = Post.objects.all().filter(community=community).order_by('-timestamp')
    return render(request, 'communityhome.html', {
        'community' : community,
        'form' : PostForm(initial={'community' : community}),
        'posts' : posts,
        'songs' : songs,
        'searchForm': SearchForm(),
        'communities' : Community.objects.all(),
        'comm_users': comm_users,
        'user_profile': user_profile,
        'comment_form': CommentForm(),
        'createCommunityForm': communityForm
    })
    
def communityVote(request, community_name):
    communityForm = createCommunityForm(request.POST)
    songs = ""
    try:
        if(request.user.is_authenticated):
            user_profile = request.user.profile
        else:
            user_profile = ""
        community = Community.objects.get(name=community_name)
        comm_users = Profile.objects.filter(joined_communities__in=[community.id]).values()
    except Community.DoesNotExist:
        raise Http404('Community not found')
    if request.method == "POST":
        if 'post_flag' in request.POST:
                form = PostForm(request.POST)
                if form.is_valid():
                    post = form.save(commit=False)
                    post.poster = request.user
                    add_songs = list(filter(None, request.POST['songs_input'].split(',')))
                    post.save()
                    print(add_songs)
                    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='616f55f94a904037a1eb6bdfbfa96d95', client_secret='2e262cfa37904ebeb74d43ff6903c9de'))
                    if(add_songs):
                        for song in add_songs:
                            try:
                                newsong = Song(song_id = song)
                                song_name = sp.track(song).get('name')
                                newsong.song_name = song_name
                                newsong.save()
                            except:
                                print("song already in library")
                            tempsong = get_object_or_404(Song, song_id = song)
                            post.songs.add(tempsong)
                    post.save()
                    return HttpResponseRedirect(request.path_info)
        if 'search_flag' in request.POST:
                searchForm = SearchForm(request.POST)
                if searchForm.is_valid():
                    query = searchForm.cleaned_data['query']
                    songs = search_songs(query)
    posts = Post.objects.all().filter(community=community).order_by('-score')
    return render(request, 'communityhome.html', {
        'community' : community,
        'form' : PostForm(initial={'community' : community}),
        'posts' : posts,
        'songs' : songs,
        'searchForm': SearchForm(),
        'communities' : Community.objects.all(),
        'comm_users': comm_users,
        'user_profile': user_profile,
        'comment_form': CommentForm(),
        'createCommunityForm': communityForm
    })


def join_community(request, community_name):
    try:
        user_profile = request.user.profile
    except Profile.DoesNotExist:
        user_profile = Profile(user=request.user)
    comm = get_object_or_404(Community, name=community_name)
    user_profile.joined_communities.add(comm)
    user_profile.save()
    return redirect('groups:home')

def leave_community(request, community_name):
    try:
        user_profile = request.user.profile
    except Profile.DoesNotExist:
        user_profile = Profile(user=request.user)
    comm = get_object_or_404(Community, name=community_name)
    user_profile.joined_communities.remove(comm)
    user_profile.save()
    return redirect('groups:home')

def rate(request, post_id, rating):
    post = Post.objects.get(id=post_id)
    if not request.user.is_authenticated:
        # Failure, not authenticated
        return HttpResponse("Votes: " + str(post.score))
    elif request.user in post.raters.all():
        # Failure, cannot rate posts twice
        return HttpResponse("Votes: " + str(post.score))
    post.score += 1 if rating > 0 else -1
    post.raters.add(request.user)
    post.save()
    return HttpResponse("Votes: " + str(post.score))

def add(request, post_id):
    post = Post.objects.get(id=post_id)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.poster = request.user
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return redirect('groups:community', community_name=post.community.name)


def createCommunity(request):
    form = createCommunityForm(request.POST)
    if form.is_valid():
        community_name = form.cleaned_data['name'] # code works up to here
    else:
        raise Http404('Something went wrong')
    communities = Community.objects.all()
    community = communities.filter(name=community_name)
    if not community:
        new_community = communities.create(name=community_name)
        new_community.save()
    return redirect('/groups')

def boom():
    return 2/0
