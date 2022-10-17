from django.urls import path
from . import views

app_name = 'hearddit'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('groups/', views.groups, name='groups'),
    path('profile/', views.profile, name='profile')
]
 