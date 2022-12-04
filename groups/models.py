from django.db import models
from django.contrib.auth.models import User
from music.models import Song


class Community(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name.title()
class Post(models.Model):
    text = models.CharField(max_length=200)
    score = models.IntegerField(default=0)
    raters = models.ManyToManyField(User, blank=True, related_name='%(class)s_requests_created')
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    songs = models.ManyToManyField(Song, blank=True)

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)