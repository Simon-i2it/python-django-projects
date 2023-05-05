from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def create(request: HttpRequest) -> HttpResponse:
    return render(request, "")


def update(request: HttpRequest) -> HttpResponse:
    return render(request, "")


def delete(request: HttpRequest) -> HttpResponse:
    return render(request, "")
