from django.http import Http404
from django.shortcuts import render

from groups.models import Post
from groups.models import Community


# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('-timestamp')
    communities = Community.objects.all();
    return render(request, 'home.html', {
        'posts': posts,
        'communities': communities,
    })
