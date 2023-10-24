from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def user_register(request):
    return HttpResponse("User Registrations Page!")
