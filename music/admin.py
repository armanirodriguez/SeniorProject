from django.contrib import admin

# Register your models here.
from .models import Song,Playlist

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    pass


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    pass