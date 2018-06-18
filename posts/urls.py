from django.urls import path
from posts.views import get_posts, post_detail, edit_post, new_post

urlpatterns = [
    path('new/', new_post, name='new_post'),
    path('<pk>/edit', edit_post, name='edit_post'),
    path('<pk>/', post_detail, name='post_detail'),
    path('', get_posts, name='get_posts'),
]
