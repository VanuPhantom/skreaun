from django.http import HttpRequest, HttpResponse

from .components import landing

# Create your views here.
def index(_: HttpRequest) -> HttpResponse:
    return HttpResponse(landing())
