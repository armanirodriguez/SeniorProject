from django.contrib import admin

from .models import Community, Post, Comment

@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass