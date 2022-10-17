from django.contrib import admin

from .models import Community, Post

@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass