from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from accounts.forms import UserRegistrationForm


def user_register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            messages.success(request, "User registration successfully!")
            return redirect("home:home")
    
    form = UserRegistrationForm()
    return render(request, "register.html", {"form": form})
