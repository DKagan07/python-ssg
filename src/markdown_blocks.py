def markdown_to_blocks(document):
    """markdown_to_blocks takes a document with blocks of MD and returns a list
    of strings, where each item in the list is a block of text"""

    blocks = document.split("\n\n")

    res = []
    for block in blocks:
        if len(block) == 0:
            continue

        block = block.strip()

        # Is this necessary?
        # block = block.replace("\n", "")
        res.append(block)

    return res
