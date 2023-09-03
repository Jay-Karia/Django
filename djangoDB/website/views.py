from django.shortcuts import render, redirect
from .models import Member
from .forms import MemberForm
from django.contrib import messages

# Create your views here.
def home(request):
    all_members = Member.objects.all()
    context = {
        "members": all_members
    }
    return render(request, "home.html", context)


def join(request):
    if request.method == "POST":
        form = MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, "There was error submitting your form")
            context = {
                "status": "error"
            }
            return redirect("/join", context)
        messages.success(request, "Member successfully joined!!")
        return redirect("/")
    return render(request, "join.html")