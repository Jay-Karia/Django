from django.http import HttpResponse

# Create your views here.
def index():
    return HttpResponse("this is index page")
