from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request): 
    context = {
        'name': "jay sanjay karia"
    }
    return render(request, "index.html",context=context)

def about(request):
    return HttpResponse("this is about page")

def contact(request):
    return HttpResponse("this is contact page")

def services(request):
    return HttpResponse("this is services page")