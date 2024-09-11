""" this module holds related HTML class definitions"""

# from enum import Enum


class HTMLNode:
    """class definition of a HTML node"""

    # class TextType(Enum):
    #

    def __init__(self, tag, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        """not implemented"""
        raise NotImplementedError()

    def props_to_html(self):
        """props_to_html makes props into a string"""

        string = ""
        if self.props is not None:
            for k, v in self.props.items():
                string += f' {k}="{v}"'
            return string
        return string

    def __repr__(self):
        return f"""
        Tag: {self.tag}
        Value: {self.value}
        Children: {self.children}
        Props: {self.props}"""

    def __eq__(self, node):
        return (
            self.tag == node.tag
            and self.value == node.value
            and self.children == node.children
            and self.props == node.props
        )


class LeafNode(HTMLNode):
    """leaf node is a leaf html node"""

    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        self.props = props

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")

        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    """parent node is a parent html node"""

    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Must have a tag")
        if self.children is None:
            raise ValueError("Must have children in a parent node")

        total_html = f"<{self.tag}>"
        for child in self.children:
            # child should be of either type LeafNode or ParentNode
            html_text = child.to_html()
            total_html += html_text
        return total_html + f"</{self.tag}>"
