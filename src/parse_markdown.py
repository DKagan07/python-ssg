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
