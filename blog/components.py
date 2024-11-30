from typing import Iterable

from htpy import Element, a, li, p, ul
from markupsafe import Markup

from common.components import content

from .models import Post


def post_list(posts: Iterable[Post]) -> Element:
    return content(
        ul[
            [
                li[
                    a(
                        {
                            "href": post.url,
                            "hx-get": post.url,
                            "hx-trigger": "click",
                            "hx-target": "main",
                            "hx-swap": "outerHTML",
                            "hx-push-url": "true",
                        }
                    )[post.title]
                ]
                for post in posts
            ]
        ],
        sub_heading="Vanu's blog",
    )


def post(post: Post) -> Element:
    return content(p[Markup(post.html)], sub_heading=post.title)
