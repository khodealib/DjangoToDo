from django.urls import path

from accounts import views

app_name = "accounts"
urlpatterns = [
    path("register/", views.user_register, name="register"),
]
