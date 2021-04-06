"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from todolist_app.views import (
    TodoListView,
    TodoCreateView,
    TodoUpdateView,
    TodoAssignUserView,
    TodoDeleteView,
    todo_done,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        '',
        TodoListView.as_view(),
        name='list_todos',
    ),
    path(
        'create/',
        TodoCreateView.as_view(),
        name='create_todo',
    ),
    path(
        'update/<int:pk>',
        TodoUpdateView.as_view(),
        name='update_todo',
    ),
    path(
        'assign_user/<int:pk>',
        TodoAssignUserView.as_view(),
        name='assign_user_todo',
    ),
    path(
        'done/<int:pk>',
        todo_done,
        name='do_todo',
    ),
    path(
        'delete/<int:pk>',
        TodoDeleteView.as_view(),
        name='delete_todo',
    ),
    path(
        'accounts/',
        include('django.contrib.auth.urls'),
        name='login_view',
    ),
]
