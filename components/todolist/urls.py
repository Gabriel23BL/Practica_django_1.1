from django.urls import path
from . import views

urlpatterns = [
    path("", views.todolist, name="to do list"),
]