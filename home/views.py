from django.http import HttpResponse
from django.http.request import HttpRequest

from django.shortcuts import render

from home.models import Todo


def home(request: HttpRequest) -> HttpResponse:
    todos = Todo.objects.all()
    return render(request, "home.html", {"todos": todos})


def say_hello(request: HttpRequest) -> HttpResponse:
    context = {
        "name": "Ali",
        "is_admin": True,
    }
    return render(request, "hello.html", context=context)
