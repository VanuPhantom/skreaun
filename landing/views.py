from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.vary import vary_on_headers

from blog.models import Post
from common.components import content, wrapper
from common.http import HttpRequest

from .components import landing


# Create your views here.
@vary_on_headers("HX-Request")
def index(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all()[:3]
    content = landing(posts)

    if not request.htmx:
        content = wrapper(content)

    return HttpResponse(content)


@vary_on_headers("HX-Request")
def page_not_found(request: HttpRequest, exception=None) -> HttpResponse:
    if request.htmx:
        return HttpResponseNotFound()
    else:
        return HttpResponseNotFound(
            wrapper(content(sub_heading="That page could not be found."))
        )
