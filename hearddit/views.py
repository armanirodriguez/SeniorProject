from django.shortcuts import render
from django.http import Http404

def home(request):
    return render(request, "hearddit/home.html")

def groups(request):
    return render(request, "hearddit/groups.html")

def profile(request):
    return render(request, "hearddit/profile.html")