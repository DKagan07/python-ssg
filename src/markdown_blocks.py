"""markdown_blocks.py holds the logic to break down blocks and tell us which
type they are"""

import re

BLOCK_HEADING = "heading"
BLOCK_PARAGRAPH = "paragraph"
BLOCK_CODE = "code"
BLOCK_QUOTE = "quote"
BLOCK_UNORDERED_LIST = "unordered_list"
BLOCK_ORDERED_LIST = "ordered_list"


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


def md_block_to_block_type(block):
    """takes a block of MD and returns a string representing what type of block it is"""

    if len(re.findall(r"^#{1,6} ", block)) > 0:
        return BLOCK_HEADING

    if len(re.findall(r"(?s)^```.*```$", block)) > 0:
        return BLOCK_CODE

    if block[0] == ">":
        return BLOCK_QUOTE

    split_blocks = block.split("\n")

    for i in range(len(split_blocks)):
        split_blocks[i] = split_blocks[i].strip()

    if len(split_blocks) > 1:
        if split_blocks[0][0] == "*" or split_blocks[0][0] == "-":
            return BLOCK_UNORDERED_LIST
        if split_blocks[0][0] == "1":
            return BLOCK_ORDERED_LIST

    return BLOCK_PARAGRAPH
