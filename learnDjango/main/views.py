from django.shortcuts import render, redirect
from .models import TodoList
from forms import CreateNewList

# Create your views here.

def getList(request, id_):
    ls = TodoList.objects.get(id=id_)

    if request.method == "POST":
        if request.POST.get("save"):
            pass
        elif request.POST.get("newItem"):
            pass

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


def create(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = TodoList(name=n)
            t.save()

            return redirect(f"/{t.id}/")

    else:
        form = CreateNewList()
    return render(request, "main/create.html", {'form':form})
