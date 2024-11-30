from typing import Iterable

from django.urls import reverse
from django.utils.http import urlencode
from htpy import Element, a, div, li, p, span, ul
from markupsafe import Markup

from common.components import content

from .models import Post


def post_list(*, posts: Iterable[Post], page: int, total_pages: int) -> Element:
    return content(
        ul[[li[post_link(post=post)] for post in posts]],
        pagination_controls(page=page, total_pages=total_pages),
        sub_heading="Vanu's blog",
    )


def post_link(*, post: Post) -> Element:
    return a(
        {
            "href": post.url,
            "hx-get": post.url,
            "hx-trigger": "click",
            "hx-target": "main",
            "hx-swap": "outerHTML",
            "hx-push-url": "true",
        }
    )[post.title]


def pagination_controls(*, page: int, total_pages: int) -> Element:
    def get_page_url(page: int) -> str:
        return "%s?%s" % (reverse("blog:index"), urlencode({"page": page - 1}))

    previous_page = get_page_url(page - 1)
    next_page = get_page_url(page + 1)

    return div(".pagination")[
        (
            a(
                {
                    "href": previous_page,
                    "hx-get": previous_page,
                    "hx-trigger": "click",
                    "hx-target": "main",
                    "hx-swap": "outerHTML",
                    "hx-push-url": "true",
                }
            )["<"]
            if page > 1
            else None
        ),
        span[f"{page}/{total_pages}"],
        (
            a(
                {
                    "href": next_page,
                    "hx-get": next_page,
                    "hx-trigger": "click",
                    "hx-target": "main",
                    "hx-swap": "outerHTML",
                    "hx-push-url": "true",
                }
            )[">"]
            if page < total_pages
            else None
        ),
    ]


def post(post: Post) -> Element:
    return content(p[Markup(post.html)], sub_heading=post.title)
