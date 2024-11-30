from django.http import HttpRequest, HttpResponse

from blog.models import Post

from .components import landing


# Create your views here.
def index(_: HttpRequest) -> HttpResponse:
    posts = Post.objects.all()[:3]

    return HttpResponse(landing(posts))
