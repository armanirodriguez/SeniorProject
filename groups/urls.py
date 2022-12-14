from django.urls import path, include
from groups import views

app_name = "groups"

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path('', views.home, name='home'),
    path('v', views.homeVote, name='homeVote'),
    path('c/<str:community_name>/', views.community, name='community'),
    path('cs/<str:community_name>/', views.communityVote, name='communityVote'),
    path("joincommunity/<str:community_name>", views.join_community, name='join_community'),
    path("leavecommunity/<str:community_name>", views.leave_community, name='leave_community'),
    path("rate/<int:post_id>/<int:rating>", views.rate, name='rate'),
    path("add/<int:post_id>", views.add, name='add'),
    path("createCommunity", views.createCommunity, name='createCommunity')
]