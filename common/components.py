from django.templatetags.static import static
from django.urls import reverse
from htpy import (
    Element,
    HTMLElement,
    Node,
    a,
    body,
    div,
    h1,
    h2,
    head,
    html,
    link,
    main,
    script,
)


def wrapper(*children: Node) -> HTMLElement:
    return html[
        head[link(rel="stylesheet", href=static("/blog/stylesheet.css"))],
        body[
            div(".container")[
                h1[a(href=reverse("landing:index"))["Vanu's site"]], children
            ],
            script(src=static("dist/htmx.min.js")),
        ],
    ]


def content(*children: Node, sub_heading: Node = None) -> Element:
    sub_heading_component: None | Node = None
    if sub_heading is not None:
        sub_heading_component = h2[sub_heading]

    return main({"hx-history-elt": True})[sub_heading_component, *children]
