from django.contrib import admin
from django.urls import path, include

from groups import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', views.home, name='home'),
    path('c/<str:community_name>/', views.community, name='community')
]
