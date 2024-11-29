from django.http import HttpRequest, HttpResponse, request
from django.shortcuts import render

# Create your views here.
def index(_: HttpRequest) -> HttpResponse:
    return HttpResponse("Landing page")
