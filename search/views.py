from django.shortcuts import render
from django.http import Http404



def search(request):
    return render(request, 'search.html', {})