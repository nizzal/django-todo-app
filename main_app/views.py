from turtle import title
from django.forms.fields import DateTimeField
from django.http import QueryDict
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from datetime import date, datetime


# Create your views here.
def home_page(request):
    q = request.GET.get("q", "")
    order_by_value = ""

    if q == "desc":
        order_by_value = "-title"
    elif q == "date":
        order_by_value = "created_at"
    else:
        order_by_value = "title"

    # filtering todo objects based on query value
    todos = Todo.objects.all().order_by(order_by_value)
    context = {"todos": todos}
    return render(request, "index.html", context)


# create-todo page
def create_todo(request):
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home_page")
    context = {"form": form, "title": "Create new todo"}
    return render(request, "todo.html", context)


# delete todo
def delete_todo(request, todo_id):
    if int(todo_id):
        Todo.objects.filter(id=todo_id).delete()
    return redirect("home_page")


# edit todos
def edit_todo(request, todo_id):
    current_todo = Todo.objects.get(id=todo_id)
    form = TodoForm(instance=current_todo)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=current_todo)
        if form.is_valid():
            form.instance.is_edited = True
            form.save()
            return redirect("home_page")
    context = {
        "id": todo_id,
        "title": "Edit Todo",
        "previous_title": "test prev",
        "form": form,
    }
    return render(request, "todo.html", context)


# test view
def test_view(request, msg):
    context = {"error_message": "Title cannot be empty ", "redirect_link": msg}
    return render(request, "error.html", context)
    # return HttpResponse("<span> Error! Title cannot be empty, redirecting to previous page, or <a href='#'>click here</a> ")
