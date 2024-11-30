from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.vary import vary_on_headers

from common.components import wrapper
from common.http import HttpRequest

from .components import post as post_display, post_list
from .models import Post


# Create your views here.
@vary_on_headers("HX-Request")
def index(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all()
    content = post_list(posts)

    if not request.htmx:
        content = wrapper(content)

    return HttpResponse(content)


def post(request: HttpRequest, post_id: int) -> HttpResponse:
    try:
        post = Post.objects.get(pk=post_id)
        content = post_display(post)

        if not request.htmx:
            content = wrapper(content)

        return HttpResponse(content)
    except Post.DoesNotExist:
        return HttpResponseNotFound()
