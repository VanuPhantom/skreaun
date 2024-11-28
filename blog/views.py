# type: ignore
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.http.response import Http404

from .components import post_list, wrapper, post as post_display
from .models import Post

# Create your views here.
def index(_: HttpRequest) -> HttpResponse:
    posts: QuerySet[Post] = Post.objects.all()
    return HttpResponse(wrapper(post_list(posts)))

def post(_: HttpRequest, post_id: int) -> HttpResponse:
    post: Post | None = Post.objects.get(pk=post_id)

    if post is None:
        return HttpResponseNotFound()
    else:
        return HttpResponse(wrapper(post_display(post)))

