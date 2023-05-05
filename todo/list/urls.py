from django.urls import path

from todo.list import views

urlpatterns = [
    path("create", views.create),
    path("update", views.update),
    path("delete", views.delete),
]
