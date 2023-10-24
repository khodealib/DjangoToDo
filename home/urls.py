from django.urls import path

from home import views

app_name = "home"
urlpatterns = [
    path("", views.home, name="home"),
    path("detail/<int:todo_id>/", views.todo_detail, name="todo_detail"),
]
