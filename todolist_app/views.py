# from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView,
    # UpdateView,
    # DeleteView,
)
from .models import Todo

# Create your views here.


class TodoListView(ListView):
    model = Todo


class TodoCreateView(CreateView):
    model = Todo
    fields = [
        'description',
        'priority',
    ]
