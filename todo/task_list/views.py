from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from .models import Task
from .forms import TaskForm


class Tasks(ListView):
    model = Task
    form_class = TaskForm
    template_name = "task_list/tasks.html"
    context_object_name = "tasks"


class AddTask(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task_list/task.html"

    def get_success_url(self) -> str:
        return reverse_lazy("url-tasks")


class UpdateTask(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task_list/task.html"

    def get_object(self) -> Task:
        pk = self.kwargs.get("pk")
        return get_object_or_404(Task, pk=pk)

    def get_success_url(self) -> str:
        return reverse_lazy("url-tasks")


def complete_task(request: HttpRequest, pk, is_completed) -> HttpResponse:
    task = Task.objects.get(pk=pk)
    if task is not None:
        task.is_completed = is_completed
        task.save()
    return redirect("url-tasks")


class DeleteTask(DeleteView):
    model = Task

    def get_object(self) -> Task:
        pk = self.kwargs.get("pk")
        return get_object_or_404(Task, pk=pk)

    def get_success_url(self) -> str:
        pk = self.kwargs.get("pk")
        return reverse("url-tasks")


def delete_task(request: HttpRequest, pk) -> HttpResponse:
    task = Task.objects.get(pk=pk)
    if task is not None:
        task.delete()
    return redirect("url-tasks")
