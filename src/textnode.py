from htmlnode import LeafNode


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, text_node) -> bool:
        return (
            self.text == text_node.text
            and self.text_type == text_node.text_type
            and self.url == text_node.url
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node):
    """text_node_to_html_node converts a text node to a leaf node, a type of html node"""

    match text_node.text_type:
        case "bold":
            return LeafNode("b", text_node.text)
        case "italic":
            return LeafNode("i", text_node.text)
        case "code":
            return LeafNode("code", text_node.text)
        case "link":
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case "image":
            return LeafNode("img", "", {"href": text_node.url, "alt": text_node.text})
        case "text":
            return LeafNode(None, text_node.text)
        case _:
            raise Exception("Not a valid text node type to convert to leaf node")
