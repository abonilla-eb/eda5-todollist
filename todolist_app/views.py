# from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Todo

# Create your views here.


class TodoListView(ListView):
    model = Todo
