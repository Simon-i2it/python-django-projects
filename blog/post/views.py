from datetime import date
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Post


def welcome(request: HttpRequest) -> HttpResponse:
    latest_posts = Post.objects.order_by("-date")[:3]
    return render(request, "post/welcome.html", {"posts": latest_posts})


def posts(request: HttpRequest) -> HttpResponse:
    return render(request, "post/posts.html", {"posts": Post.objects.order_by("-date")})


def post(request: HttpRequest, slug) -> HttpResponse:
    correct_post = get_object_or_404(Post, slug=slug)
    return render(request, "post/post-detail.html", {"post": correct_post})
