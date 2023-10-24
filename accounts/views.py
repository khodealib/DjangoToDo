from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from accounts.forms import UserLoginForm, UserRegistrationForm


def user_register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )
            user.first_name = form.cleaned_data["first_name"]
            user.last_name = form.cleaned_data["last_name"]
            user.save()
            messages.success(request, "User registration successfully!")
            return redirect("home:home")

    form = UserRegistrationForm()
    return render(request, "register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully!")
                return redirect("home:home")
            messages.error(request, "username or password is wrong!")

    form = UserLoginForm()
    return render(request, "login.html", {"form": form})


def user_logout(request):
    if not request.user.is_authenticated:
        messages.error(request, "Your not logged in user!")
        return redirect("home:home")

    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("home:home")
