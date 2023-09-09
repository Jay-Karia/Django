from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, UpdateForm
from django.urls import reverse_lazy

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = "blogApp/home.html"
    ordering = '-id'

class ArticleDetailView(DetailView):
    model = Post
    template_name = "blogApp/details.html"


class CreateBlogView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "blogApp/create.html"

class UpdatePostView(UpdateView):
    model = Post
    template_name = "blogApp/edit.html"
    form_class = UpdateForm

class DeletePostView(DeleteView):
    model = Post
    template_name = "blogApp/delete.html"
    success_url = reverse_lazy("home")
