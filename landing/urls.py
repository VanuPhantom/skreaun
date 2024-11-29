from django.urls import URLPattern, URLResolver, path

from . import views

app_name = "landing"
urlpatterns: list[URLResolver | URLPattern] = [
    path("", views.index, name="index"),
]
