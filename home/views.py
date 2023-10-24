from django.contrib import messages
from django.http import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import redirect, render

from home.forms import TodoCreateForm, TodoUpdateForm
from home.models import Todo


def home(request: HttpRequest) -> HttpResponse:
    todos = Todo.objects.all()
    return render(request, "home.html", {"todos": todos})


def todo_detail(request: HttpRequest, todo_id: int) -> HttpResponse:
    todo = Todo.objects.get(id=todo_id)
    return render(request, "detail.html", {"todo": todo})


def todo_delete(request, todo_id: int):
    """
    send extra tags for css style in django use extra on messages
    messages.success(request, "TodoModel deleted successfully!", "success")
    and use in django templated with message.tags
    this here we use bootstrap messages!
    """
    Todo.objects.get(id=todo_id).delete()
    messages.success(request, "Todo deleted successfully!")
    return redirect("home:home")


def todo_create(request):
    if request.method == "POST":
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            Todo.objects.create(
                title=form.cleaned_data["title"],
                body=form.cleaned_data["body"],
                created=form.cleaned_data["created"],
            )
            messages.success(request, "Todo created successfully!")
            return redirect("home:home")
    
    form = TodoCreateForm()
    return render(request, "create.html", {"form": form})


def todo_update(request, todo_id: int):
    todo = Todo.objects.get(id=todo_id)
    if request.method == "POST":
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, "Todo updated successfully!")
            return redirect("home:todo_detail", todo_id)
    
    form = TodoUpdateForm(instance=todo)
    return render(request, "update.html", {"form": form, "todo_id": todo.id})
