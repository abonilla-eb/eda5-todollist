from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse
from .models import Todo
from django.shortcuts import redirect

# Create your views here.


class TodoListView(ListView):
    model = Todo


class TodoCreateView(CreateView, LoginRequiredMixin):
    model = Todo
    fields = [
        'description',
        'priority',
    ]

    def get_success_url(self):
        return reverse('list_todos')

    def form_valid(self, form):
        form.instance.user_assigned = self.request.user
        return super(TodoCreateView, self).form_valid(form)


class TodoUpdateView(UpdateView, LoginRequiredMixin):
    model = Todo
    fields = '__all__'
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('list_todos')


class TodoDeleteView(DeleteView, LoginRequiredMixin):
    model = Todo

    def get_success_url(self):
        return reverse('list_todos')


def todo_done(request, pk):
    # self.done = True
    # return reverse('list_todos')
    done_todo = Todo.objects.get(pk=pk)
    done_todo.done = True
    done_todo.save()
    return redirect('list_todos')
