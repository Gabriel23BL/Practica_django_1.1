from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello, name="hola_mundo"),
]