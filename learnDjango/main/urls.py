from django.urls import path, include
from . import views

urlpatterns = [
    path("<int:id_>/", views.getList, name="getList"),
    path("", views.home, name="home"),
]
