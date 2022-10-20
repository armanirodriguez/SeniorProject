from django.db import models

# Create your models here.

class Song(models.Model):
    song_id = models.CharField(max_length=100)
    song_name = models.CharField(max_length=50)