from django.http import HttpResponse
from django.http.request import HttpRequest

from django.shortcuts import render

from home.models import Todo


def home(request: HttpRequest) -> HttpResponse:
    todos = Todo.objects.all()
    return render(request, "home.html", {"todos": todos})


def todo_detail(request: HttpRequest, todo_id: int) -> HttpResponse:
    todo = Todo.objects.get(id=todo_id)
    return render(request, "detail.html", {"todo": todo})
