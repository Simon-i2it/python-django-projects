from datetime import date
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from post.models import Post

# Create your views here.


def welcome(request: HttpRequest) -> HttpResponse:
    breakpoint()
    latest_posts = Post.objects.order_by("-date")[:3]
    return render(request, "blog/welcome.html", {"posts": latest_posts})
