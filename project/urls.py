
from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path("als/", include("als.urls")),
    path('admin/', admin.site.urls),
]
