from django.http import HttpRequest, HttpResponse, HttpResponseNotFound

from .components import post_list, wrapper, post as post_display
from .models import Post


# Create your views here.
def index(_: HttpRequest) -> HttpResponse:
    posts = Post.objects.all()
    return HttpResponse(wrapper(post_list(posts)))


def post(_: HttpRequest, post_id: int) -> HttpResponse:
    try:
        post = Post.objects.get(pk=post_id) 
        return HttpResponse(wrapper(post_display(post)))
    except Post.DoesNotExist:
        return HttpResponseNotFound()
