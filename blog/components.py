from typing import Iterable
from htpy import Element, HTMLElement, body, h1, html, p, main, ul, li
from .models import Post

def wrapper(*children: list[Element]) -> HTMLElement:
    return html[body[h1["Vanu's blog"], main[*children]]]

def post_list(posts: Iterable[Post]) -> Element:
    return ul[[li[str(post.title)] for post in posts]]

