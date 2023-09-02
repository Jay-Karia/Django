from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Site Admin"
admin.site.site_title = "Site Admin Portal"
admin.site.index_title = "Welcome to Site Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("myApp.urls")),
]
