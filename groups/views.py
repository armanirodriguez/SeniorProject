from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.http import Http404

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from .models import Community, Post
from .forms import PostForm

from search.forms import SearchForm

def home(request):
    songs = ""
    if request.method == "POST":
        if 'post_flag' in request.POST:
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.poster = request.user
                post.save()
                return HttpResponseRedirect(request.path_info)
        if 'search_flag' in request.POST:
            searchForm = SearchForm(request.POST)
            if searchForm.is_valid():
                query = searchForm.cleaned_data['query']
                songs = search_songs(query)                
    posts = Post.objects.all().order_by('-timestamp')
    return render(request, 'communityhome.html', {
        'form' : PostForm(),
        'posts' : posts,
        'communities' : Community.objects.all(),
        'searchForm': SearchForm(),
        'songs': songs
    })

def search_songs(query):
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='616f55f94a904037a1eb6bdfbfa96d95', client_secret='2e262cfa37904ebeb74d43ff6903c9de'))
    result = sp.search(q=query, type="track", limit=1)['tracks']['items']
    tracks = [item['id'] for item in result]
    return tracks

def community(request, community_name):
    try:
        community = Community.objects.get(name=community_name)
    except Community.DoesNotExist:
        raise Http404('Community not found')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.poster = request.user
            post.save()
    posts = Post.objects.all().filter(community=community).order_by('-timestamp')
    return render(request, 'communityhome.html', {
        'community' : community,
        'form' : PostForm(initial={'community' : community}),
        'posts' : posts,
        'communities' : Community.objects.all()
    })