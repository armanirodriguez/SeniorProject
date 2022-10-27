from django.shortcuts import render
from django.http import Http404
from .forms import SearchForm



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
    return []