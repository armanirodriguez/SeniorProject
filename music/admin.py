from django.contrib import admin

# Register your models here.
from .models import Song

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    pass