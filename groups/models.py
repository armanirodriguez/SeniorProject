from django.db import models
from django.contrib.auth.models import User
from music.models import Song



class Community(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name.title()
class Post(models.Model):
    text = models.CharField(max_length=200)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    song = models.OneToOneField(Song, on_delete=models.DO_NOTHING, blank=True, null=True)