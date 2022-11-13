from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .forms import SearchForm
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from music.models import Song
from users.models import Profile
from django.db import IntegrityError

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            songs = search_songs(query)
            return render(request, 'search.html', {'form': form, 'songs': songs})
        else:
            raise Http404('Something went wrong')
    else:
        form = SearchForm()
        return render(request, 'search.html', {'form': form})

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