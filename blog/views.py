from django.http import HttpRequest, HttpResponse, HttpResponseNotFound

from .components import post as post_display, post_list
from .models import Post


# Create your views here.
def index(_: HttpRequest) -> HttpResponse:
    posts = Post.objects.all()
    return HttpResponse(post_list(posts))


def post(_: HttpRequest, post_id: int) -> HttpResponse:
    try:
        post = Post.objects.get(pk=post_id)
        return HttpResponse(post_display(post))
    except Post.DoesNotExist:
        return HttpResponseNotFound()
