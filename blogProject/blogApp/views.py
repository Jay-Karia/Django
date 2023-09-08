from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = "blogApp/home.html"


class ArticleDetailView(DetailView):
    model = Post
    template_name = "blogApp/details.html"
