from django.urls import URLPattern, URLResolver, path

from . import views

urlpatterns: list[URLResolver | URLPattern] = [
        path("", views.index, name="index")
        ]
