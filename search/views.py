from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .forms import SearchForm,ListForm
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from music.models import Song,Playlist
from users.models import Profile
from django.db import IntegrityError

def search(request):
    searchform = SearchForm(request.POST)
    listform = ListForm(request.POST)
    
    if request.method == 'POST':
        if searchform.is_valid():
            query = searchform.cleaned_data['query']
            songs = search_songs(query)
            if request.user.is_authenticated:
                profile = request.user.profile
                playlists = profile.playlists.all()
                return render(request, 'search.html', {'searchform': searchform, 'listform':listform, 'songs': songs, 'playlists':playlists})
            return render(request, 'search.html', {'searchform': searchform, 'listform':listform, 'songs': songs})
        else:
            raise Http404('Something went wrong')
    else:
        searchform = SearchForm()
        if request.user.is_authenticated:
                profile = request.user.profile
                playlists = profile.playlists.all()
                return render(request, 'search.html', {'searchform': searchform, 'listform':listform, 'playlists':playlists})
        return render(request, 'search.html', {'searchform': searchform,'listform':listform})

def search_songs(query):
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='616f55f94a904037a1eb6bdfbfa96d95', client_secret='2e262cfa37904ebeb74d43ff6903c9de'))
    result = sp.search(q=query, type="track", limit=5)['tracks']['items']
    tracks = [item['id'] for item in result]
    return tracks

def fave_song(request, song_id):
    try:
        user_profile = request.user.profile
    except Profile.DoesNotExist:
        user_profile = Profile(user=request.user)
    print(song_id)
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='616f55f94a904037a1eb6bdfbfa96d95', client_secret='2e262cfa37904ebeb74d43ff6903c9de'))
    song_name = sp.track(song_id).get('name')
    print(song_name)
    newSong = Song(song_id=song_id, song_name=song_name)
    try:
        newSong.save()
        user_profile.fave_songs.add(newSong)
        user_profile.save()
    except:
        print("song already in library")
    
    tempsong = get_object_or_404(Song, song_id=song_id)
    if not(tempsong in user_profile.fave_songs.all()):
        user_profile.fave_songs.add(tempsong)
        user_profile.save()
       
    return redirect('/users/profile/')

def addtolist(request, song_id):
    try:
        user_profile = request.user.profile
    except Profile.DoesNotExist:
        user_profile = Profile(user=request.user)
    print(song_id)
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='616f55f94a904037a1eb6bdfbfa96d95', client_secret='2e262cfa37904ebeb74d43ff6903c9de'))
    song_name = sp.track(song_id).get('name')
    print(song_name)
    newSong = Song(song_id=song_id, song_name=song_name)
    
    listForm = ListForm(request.POST)
    if listForm.is_valid():
        playlistname = listForm.cleaned_data['Playlist']
    else:
        raise Http404('Something went wrong')
    playlist = playlistname
    try:
        newSong.save()
        playlist.songs.add(newSong)
        playlist.save()
    except:
        print("song already in playlist")
    
    tempsong = get_object_or_404(Song, song_id=song_id)
    if not(tempsong in playlist.songs.all()):
        playlist.songs.add(tempsong)
        playlist.save()
        
    return redirect('/search/')

def removePlaySong(request, playlist_name, song_id):
    try:
        user_profile = request.user.profile
    except Profile.DoesNotExist:
        user_profile = Profile(user=request.user)
    playlists = user_profile.playlists.all()
    playlist = playlists.filter(playlist_name=playlist_name).first()
    print(playlist)
    tempsong = get_object_or_404(Song, song_id = song_id)
    playlist.songs.remove(tempsong)
    return redirect('/search')

def removePlayList(request, playlist_name):
    try:
        user_profile = request.user.profile
    except Profile.DoesNotExist:
        user_profile = Profile(user=request.user)
    playlists = user_profile.playlists.all()
    playlist = playlists.filter(playlist_name=playlist_name).first()
    playlist.delete()
    return redirect('/search')