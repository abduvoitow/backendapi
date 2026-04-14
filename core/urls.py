from django.urls import path
from .views import get_posts, create_post

urlpatterns = [
    path('posts/', get_posts),
    path('posts/create/', create_post),
]
