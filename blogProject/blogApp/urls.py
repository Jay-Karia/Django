from django.urls import path
from .views import HomeView, ArticleDetailView, CreateBlogView, UpdatePostView, DeletePostView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("article/<int:pk>", ArticleDetailView.as_view(), name="article-detail"),
    path("create/", CreateBlogView.as_view(), name="create"),
    path("edit/<int:pk>", UpdatePostView.as_view(), name="update"),
    path("delete/<int:pk>/", DeletePostView.as_view(), name="delete")
]
