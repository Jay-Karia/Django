from django.shortcuts import render
from .models import TodoList


# Create your views here.

def getList(request, id_):
    ls = TodoList.objects.get(id=id_)
    context = {
        'title': f"Todo {id_}",
        'list': ls,
        "name": ls.name
    }
    return render(request, "main/todolist.html", context)


def home(request):
    context = {
        'title': "custom title from views file"
    }
    return render(request, "main/home.html", context)
