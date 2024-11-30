from typing import Iterable

from django.urls import reverse
from htpy import Element, Node, a, b, h2, li, p, ul

from blog.models import Post
from common.components import wrapper


def intro() -> Element:
    return p[
        "Hi there! I'm ",
        b["Vanu"],
        ", and this is my personal site! You can find ",
        a(href="https://github.com/VanuPhantom/skreaun")["it's source code on GitHub"],
        ".",
    ]


def contact() -> Node:
    return [
        h2["Where to find me"],
        ul[
            [
                li[a(href=url)[text]]
                for url, text in [
                    (
                        "https://zug.network/@VanuPhantom",
                        "@VanuPhantom@zug.network",
                    ),
                    ("https://github.com/VanuPhantom", "github.com/VanuPhantom"),
                    (
                        "https://soundcloud.com/VanuPhantom",
                        "soundcloud.com/VanuPhantom",
                    ),
                ]
            ]
        ],
    ]


def blog(posts: Iterable[Post]) -> Node:
    return [
        h2["Blog"],
        ul[[li[post.title] for post in posts]],
        p[a(href=reverse("blog:index"))["More posts..."]],
    ]


def landing(posts: Iterable[Post]) -> Element:
    return wrapper(intro(), contact(), blog(posts))
