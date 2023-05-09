from datetime import date
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

from .forms import PostForm
from .models import Post


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
        # if form.is_valid():
        # post = form.save(commit=False)
        data = request.POST
        for image in request.FILES.getlist("image"):
            print(data["title"])
            print(data["summary"])
            print(data["content"])
            Post.objects.create(
                title=data["title"],
                summary=data["summary"],
                content=data["content"],
                author=request.user,
                image=image,
            )
        # else:
        #     return render(
        #         request,
        #         "post/post.html",
        #         {"form": form, "errors": list(form.errors.values())},
        #     )

    return render(request, "post/post.html", {"form": form})
