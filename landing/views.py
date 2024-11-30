from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.vary import vary_on_headers

from blog.models import Post
from common.components import content, wrapper
from common.http import HttpRequest

from .components import landing


# Create your views here.
def index(_: HttpRequest) -> HttpResponse:
    posts = Post.objects.all()[:3]

    return HttpResponse(landing(posts))


@vary_on_headers("HX-Request")
def page_not_found(request: HttpRequest, exception = None) -> HttpResponse:
    if request.htmx:
        return HttpResponseNotFound()
    else:
        return HttpResponseNotFound(
            wrapper(content(sub_heading="That page could not be found."))
        )
