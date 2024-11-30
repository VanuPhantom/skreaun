from typing import Iterable

from django.urls import reverse
from htpy import Element, Node, a, b, h2, li, p, ul

from blog.models import Post
from blog.components import post_link
from common.components import content, wrapper


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
    blog_url = reverse("blog:index")

    return [
        h2["Blog"],
        ul[[li[post_link(post=post)] for post in posts]],
        p[
            a(
                {
                    "href": blog_url,
                    "hx-get": blog_url,
                    "hx-target": "main",
                    "hx-swap": "outerHTML",
                    "hx-push-url": "true",
                }
            )["More posts..."]
        ],
    ]


def landing(posts: Iterable[Post]) -> Element:
    return wrapper(content(intro(), contact(), blog(posts)))
