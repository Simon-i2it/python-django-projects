from datetime import date
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

from .forms import PostForm
from .models import Author, Post


def welcome(request: HttpRequest) -> HttpResponse:
    latest_posts = Post.objects.order_by("-date")[:3]
    return render(request, "post/welcome.html", {"posts": latest_posts})


def posts(request: HttpRequest) -> HttpResponse:
    return render(request, "post/posts.html", {"posts": Post.objects.order_by("-date")})


def post(request: HttpRequest, pk: int) -> HttpResponse:
    correct_post = get_object_or_404(Post, pk=pk)
    return render(request, "post/post-detail.html", {"post": correct_post})


@login_required(login_url="url-signin")
def new_post(request: HttpRequest) -> HttpResponse:
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            data = request.POST
            author, created = Author.objects.get_or_create(account=request.user)

            image = request.FILES.get("image")

            Post.objects.create(
                title=data["title"],
                description=data["description"],
                content=data["content"],
                image=image,
                author=author,
            )

            return redirect("url-posts")
        else:
            errors = {field: error_list for field, error_list in form.errors.items()}
            return render(
                request,
                "post/post.html",
                {"form": form, "errors": errors},
            )

    return render(request, "post/post.html", {"form": form})
