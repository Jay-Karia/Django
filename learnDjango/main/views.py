from django.http import HttpResponse
from .models import TodoList, Item

# Create your views here.
def index(request):
    return HttpResponse("hello world")


def getList(request, id_):
    ls = TodoList.objects.get(id=id_)
    items = ls.item_set.get(id=1)
    return HttpResponse(f"<h1>{ls}</h1><p>{items}</p>")
