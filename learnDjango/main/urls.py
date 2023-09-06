from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("v1/", views.v1, name="v1")
]
