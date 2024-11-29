from htpy import Element, Node, a, b, h2, li, p, ul

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
            li[a(href="https://zug.network/@VanuPhantom")["@VanuPhantom@zug.network"]],
            li[a(href="https://github.com/VanuPhantom")["github.com/VanuPhantom"]],
            li[
                a(href="https://soundcloud.com/VanuPhantom")[
                    "soundcloud.com/VanuPhantom"
                ]
            ],
        ],
    ]


def landing() -> Element:
    return wrapper(intro(), contact())
