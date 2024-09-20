import re
from textnode import TextNode


# As part of making this simple, the functionality of this function is limited
# to not having nested inline elements (ex. "This is an *italic and **bold**
# word*.")
def split_nodes_with_delimiter(old_nodes, delimiter, text_type):
    """
    old_nodes is a list of text_nodes
    delimiter is the delimiter in which to split the text
    text_type is what the new nodes should be
    return: a list of new text_nodes
    """

    result = []
    for node in old_nodes:
        if node.text_type != "text":
            result.append(node)
            continue

        sp = node.text.split(delimiter)

        new_nodes = []
        if len(sp) % 2 == 0:
            raise ValueError(
                "No closing delimiter noted in this node. There must be a closing delimiter"
            )

        # if there's only 1 item that's within the delimiter, it will always have a length of 3

        for i in enumerate(sp):
            idx = i[0]
            if sp[idx] == "":
                continue

            if idx % 2 == 0:
                new_nodes.append(TextNode(sp[idx], node.text_type))
            else:
                new_nodes.append(TextNode(sp[idx], text_type))

        result.extend(new_nodes)

    return result


def extract_markdown_images(text):
    """extract_markdown_images takes raw markdown for images and returns
    a list of tuples following the format: [(alt-text, link), ...]"""

    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    """extract_markdown_links takes raw markdown for links and returns a list of
    tuples following the format: [(anchor_text, url), ...]"""

    # the difference here between the images and the links is that the links
    # regex makes sure that the alt text in the [] isn't preceeded by a "!" like
    # the images syntax
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)


def split_nodes_images(old_nodes):
    """split_nodes_images splits a TextNode with to a list of text and image nodes"""

    result = []
    for old_node in old_nodes:
        if old_node.text_type != "text":
            result.append(old_node)
            continue

        text = old_node.text

        links = extract_markdown_images(text)
        if len(links) == 0:
            result.append(old_node)
            continue

        for link in links:
            sections = text.split(f"![{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")

            if sections[0] != "":
                result.append(TextNode(sections[0], "text"))

            result.append(TextNode(link[0], "image", link[1]))

            text = sections[1]

        if text != "":
            result.append(TextNode(text, "text"))

    return result


def split_nodes_link(old_nodes):
    """split_nodes_link splits a TextNode to a list of text and link nodes"""
    result = []
    for old_node in old_nodes:
        if old_node.text_type != "text":
            result.append(old_node)
            continue

        text = old_node.text

        links = extract_markdown_links(text)
        if len(links) == 0:
            result.append(old_node)
            continue

        for link in links:
            sections = text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")

            if sections[0] != "":
                result.append(TextNode(sections[0], "text"))

            result.append(TextNode(link[0], "link", link[1]))

            text = sections[1]

        if text != "":
            result.append(TextNode(text, "text"))

    return result


def text_to_textnodes(text):
    node = TextNode(text, "text")
    nodes = split_nodes_link([node])
    nodes = split_nodes_images(nodes)
    nodes = split_nodes_with_delimiter(nodes, "**", "bold")
    nodes = split_nodes_with_delimiter(nodes, "*", "italic")
    nodes = split_nodes_with_delimiter(nodes, "`", "code")
    return nodes
