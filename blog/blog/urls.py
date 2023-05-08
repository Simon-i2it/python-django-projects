from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.welcome),
    path("blog/welcome", views.welcome, name="url-welcome"),
]
