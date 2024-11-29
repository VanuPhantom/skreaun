from typing import Iterable

from django.urls import reverse
from htpy import (
    Element,
    HTMLElement,
    a,
    body,
    div,
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
from markupsafe import Markup

from .models import Post

from django.templatetags.static import static


def wrapper(*children: Element) -> HTMLElement:
    return html[
        head[link(rel="stylesheet", href=static("/blog/stylesheet.css"))],
        body[div(".container")[h1[a(href=reverse("blog:index"))["Vanu's blog"]], *children]],
    ]


def post_list(posts: Iterable[Post]) -> Element:
    return main[ul[[li[a({"href": post.url})[post.title]] for post in posts]]]


def post(post: Post) -> Element:
    return main[h2[str(post.title)], p[Markup(post.html)]]
