from django.http import HttpRequest, HttpResponse
from htpy import HTMLElement, html,body,h1,p

# Create your views here.
def index(_: HttpRequest) -> HttpResponse:
    content: HTMLElement = html[body[h1["Skreaun"], p["Skreaun is Vanu's new blogging engine"]]]
    return HttpResponse(content) # type: ignore
