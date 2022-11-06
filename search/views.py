from django.shortcuts import render
from django.http import Http404
from .forms import SearchForm
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def boom():
    return 1/0

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