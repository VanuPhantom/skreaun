from typing import Iterable

from htpy import (
    Element,
    HTMLElement,
    a,
    body,
    h1,
    h2,
    html,
    li,
    main,
    p,
    ul,
    head,
    link,
)

from .models import Post

from django.templatetags.static import static


def wrapper(*children: list[Element]) -> HTMLElement:
    return html[
        head[link(rel="stylesheet", href=static("/blog/stylesheet.css"))],
        body[h1["Vanu's blog"], *children],
    ]


def post_list(posts: Iterable[Post]) -> Element:
    return main[ul[[li[a({"href": post.url})[str(post.title)]] for post in posts]]]


def post(post: Post) -> Element:
    return main[h2[str(post.title)], p[str(post.content)]]
