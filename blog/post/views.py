from datetime import date
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Post

# Create your views here.


def posts(request: HttpRequest) -> HttpResponse:
    return render(request, "blog/posts.html", {"posts": Post.objects.order_by("-date")})


def post(request: HttpRequest, slug) -> HttpResponse:
    correct_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {"post": correct_post})
