from typing import Iterable

from htpy import Element, a, li, p, ul
from markupsafe import Markup

from common.components import wrapper

from .models import Post


def post_list(posts: Iterable[Post]) -> Element:
    return wrapper(
        ul[[li[a({"href": post.url})[post.title]] for post in posts]],
        sub_heading="Vanu's blog",
    )


def post(post: Post) -> Element:
    return wrapper(p[Markup(post.html)], sub_heading=post.title)
