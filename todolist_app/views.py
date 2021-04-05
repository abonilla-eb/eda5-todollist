# from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse
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

    def get_success_url(self):
        return reverse('list_todos')


class TodoUpdateView(UpdateView):
    model = Todo
    fields = '__all__'
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('list_todos')


class TodoDeleteView(DeleteView):
    model = Todo

    def get_success_url(self):
        return reverse('list_todos')
