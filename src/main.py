"""main module docstring"""

from htmlnode import HTMLNode
from textnode import TextNode


def main():
    """main func docstring"""

    text_node = TextNode("This is a text node", "bold", "https://www.google.com")
    print(text_node)

    html_node = HTMLNode(
        "a",
        "this is an anchor tag",
        props={"href": "https://www.google.com", "target": "_blank"},
    )
    print("html node: ", html_node)


main()
