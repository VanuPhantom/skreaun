from django.http import Http404, HttpResponse
from django.views.decorators.vary import vary_on_headers

from common.components import wrapper
from common.http import HttpRequest

from .components import post as post_display, post_list
from .models import Post


# Create your views here.
@vary_on_headers("HX-Request")
def index(request: HttpRequest) -> HttpResponse:
    raw_page_index = request.GET.get("page", "0")
    page_index = int(raw_page_index) if raw_page_index.isdecimal() else 0

    posts = Post.objects.all()[page_index * 20 : (page_index + 1) * 20]

    total_posts = Post.objects.count()
    total_pages = total_posts // 20 + (1 if total_posts % 20 > 0 else 0)

    content = post_list(posts=posts, page=page_index + 1, total_pages=total_pages)

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
        raise Http404("This post does not exist.")
