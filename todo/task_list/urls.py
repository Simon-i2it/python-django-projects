from django.urls import path

from . import views

urlpatterns = [
    path("tasks", views.Tasks.as_view(), name="url-tasks"),
    path("task/add", views.AddTask.as_view(), name="url-add-task"),
    path("task/<pk>", views.UpdateTask.as_view(), name="url-update-task"),
    path("task/<pk>/delete", views.DeleteTask.as_view(), name="url-delete-task"),
    path("tasks/delete", views.delete_tasks, name="url-delete-tasks"),
    path(
        "task/<pk>/<is_completed>",
        views.complete_task,
        name="url-complete-task",
    ),
]
