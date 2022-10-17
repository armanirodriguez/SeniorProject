from django.http import Http404
from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request, "home.html")