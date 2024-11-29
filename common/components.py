from django.templatetags.static import static
from django.urls import reverse
from htpy import Element, HTMLElement, a, body, div, h1, h2, head, html, link, main


def wrapper(
    *children: Element, sub_heading: Element | str | None = None
) -> HTMLElement:
    sub_heading_component: None | Element = None
    if sub_heading is not None:
        sub_heading_component = h2[sub_heading]

    return html[
        head[link(rel="stylesheet", href=static("/blog/stylesheet.css"))],
        body[
            div(".container")[
                h1[a(href=reverse("landing:index"))["Vanu's site"]],
                main[sub_heading_component, *children],
            ]
        ],
    ]
