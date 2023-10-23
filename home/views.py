from django.http import HttpResponse
from django.http.request import HttpRequest

from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html")


def say_hello(request: HttpRequest) -> HttpResponse:
    return render(request, "hello.html")
