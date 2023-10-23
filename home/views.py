from django.http import HttpResponse
from django.http.request import HttpRequest

# from django.shortcuts import render


def say_hello(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello World")
