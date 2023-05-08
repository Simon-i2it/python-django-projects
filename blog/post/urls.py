from django.urls import path

from . import views

urlpatterns = [
    path("", views.welcome),
    path("welcome", views.welcome, name="url-welcome"),
    path("posts", views.posts, name="url-posts"),
    path("post/new", views.NewPost.as_view(), name="url-new-post"),
    path("post/<slug:slug>", views.post, name="url-post"),
]
