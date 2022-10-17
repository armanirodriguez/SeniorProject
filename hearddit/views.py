from django.http import Http404
from django.shortcuts import render
from .models import Community, Post
from .forms import PostForm
# Create your views here.
def home(request):
    return render(request, "home.html")

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
    return render(request, 'community.html', {
        'community' : community,
        'form' : PostForm(initial={'community' : community}),
        'posts' : posts,
        'communities' : Community.objects.all()
    })