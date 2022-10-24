from django.http import Http404
from django.shortcuts import render

from groups.models import Post
# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('-timestamp')
    return render(request, 'home.html', {
        'posts' : posts
    })