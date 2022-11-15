from django.urls import path, include
from search import views

app_name = "search"

urlpatterns = [
    path('', views.search, name='search'),
    path("faveSong/<str:song_id>", views.fave_song, name='fave_song')
]