from django.urls import path

from home import views

app_name = "home"
urlpatterns = [
    path("", views.home, name="home"),
    path("detail/<int:todo_id>/", views.todo_detail, name="todo_detail"),
    path("detail/<int:todo_id>/delete/", views.todo_delete, name="todo_delete"),
    path("detail/<int:todo_id>/update/", views.todo_update, name="todo_update"),
    path("create/", views.todo_create, name="todo_create"),
]
