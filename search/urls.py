from django.urls import path, include
from search import views

app_name = "search"

urlpatterns = [
    path('', views.search, name='search'),
]