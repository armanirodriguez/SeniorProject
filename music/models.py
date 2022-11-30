from django.db import models

# Create your models here.

class Song(models.Model):
    song_id = models.CharField(max_length=100, unique=True)
    song_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.song_name
    
class Playlist(models.Model):
    playlist_name = models.CharField(max_length=100)
    playlist_creator = models.CharField(max_length=100)
    songs = models.ManyToManyField(Song)
    
    def __str__(self):
        return self.playlist_name