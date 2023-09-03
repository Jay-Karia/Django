from django.shortcuts import render
from .models import Member

# Create your views here.
def home(request):
    all_members = Member.objects.all()
    context = {
        "members": all_members
    }
    return render(request, "home.html", context)
