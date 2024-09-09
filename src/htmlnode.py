class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        """props_to_html makes props into a string"""

        string = " "
        if self.props is not None:
            for k, v in self.props.items():
                string += f'{k}="{v}" '
            return string.rstrip()
        return string

    def __repr__(self):
        return f"""
        Tag: {self.tag}
        Value: {self.value}
        Children: {self.children}
        Props: {self.props}"""
