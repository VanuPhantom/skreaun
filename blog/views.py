# type: ignore
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse

from .components import post_list, wrapper
from .models import Post

# Create your views here.
def index(_: HttpRequest) -> HttpResponse:
    posts: QuerySet[Post] = Post.objects.all()
    return HttpResponse(wrapper(post_list(posts)))

