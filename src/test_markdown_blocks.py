import unittest

from markdown_blocks import (
    BLOCK_HEADING,
    BLOCK_ORDERED_LIST,
    BLOCK_CODE,
    BLOCK_PARAGRAPH,
    BLOCK_UNORDERED_LIST,
    markdown_to_blocks,
    md_block_to_block_type,
)


class TestMDBlockToText(unittest.TestCase):
    def test_single_block(self):
        text = """# Heading

        Paragraph
        """

        res = ["# Heading", "Paragraph"]

        self.assertListEqual(res, markdown_to_blocks(text))

    def test_multiple_returns(self):
        text = """# Heading


        Paragraph
        """

        res = ["# Heading", "Paragraph"]

        self.assertListEqual(res, markdown_to_blocks(text))

    def test_multiple_blocks_with_multiple_returns(self):
        text = """# Heading




        Paragraph 1



        Paragraph 2
        """

        res = ["# Heading", "Paragraph 1", "Paragraph 2"]

        self.assertListEqual(res, markdown_to_blocks(text))


class TestMDBlockToBlockType(unittest.TestCase):
    def test_multiple_block_types(self):
        text_block = """### Heading

        Paragraph


        ```
        This is a code block
        ```

        * list 1
        * list 2
        * list 3


        1. ordered 1
        2. ordered 2
        3. ordered 3
        
        """

        res = [
            BLOCK_HEADING,
            BLOCK_PARAGRAPH,
            BLOCK_CODE,
            BLOCK_UNORDERED_LIST,
            BLOCK_ORDERED_LIST,
        ]

        blocks = markdown_to_blocks(text_block)

        for idx, block in enumerate(blocks):
            r = md_block_to_block_type(block)
            self.assertEqual(res[idx], r)
