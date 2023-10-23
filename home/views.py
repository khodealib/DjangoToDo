from django.http import HttpResponse
from django.http.request import HttpRequest

from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html")


def say_hello(request: HttpRequest) -> HttpResponse:
    context = {
        "name": "Ali",
        "is_admin": True,
    }
    return render(request, "hello.html", context=context)
