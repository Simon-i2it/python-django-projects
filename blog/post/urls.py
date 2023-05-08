from django.urls import path

from . import views

urlpatterns = [
    path("all", views.posts, name="url-posts"),
    path("<slug:slug>", views.post, name="url-post"),
]
