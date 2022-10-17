from django.urls import path, include
from groups import views

app_name = "groups"

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path('', views.home, name='home'),
    path('c/<str:community_name>/', views.community, name='community')
]