from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse
from .models import Todo
from django.shortcuts import redirect
from .forms import TodoCreateForm

# Create your views here.


class TodoListAllView(LoginRequiredMixin, ListView):
    model = Todo


class TodoListMineView(LoginRequiredMixin, ListView):
    model = Todo

    def get_queryset(self):
        self.queryset = Todo.objects.filter(user_assigned=self.request.user)
        return super(TodoListMineView, self).get_queryset()


class TodoCreateView(LoginRequiredMixin, CreateView):
    form_class = TodoCreateForm
    model = Todo

    def get_success_url(self):
        return reverse('list_todos')

    def form_valid(self, form):
        form.instance.user_assigned = self.request.user
        return super(TodoCreateView, self).form_valid(form)


class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = '__all__'
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('list_todos')


class TodoAssignUserView(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = ['user_assigned']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('list_todos')


class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo

    def get_success_url(self):
        return reverse('list_todos')


@login_required
def todo_done(request, pk):
    # self.done = True
    # return reverse('list_todos')
    done_todo = Todo.objects.get(pk=pk)
    done_todo.done = True
    done_todo.save()
    return redirect('list_todos')
