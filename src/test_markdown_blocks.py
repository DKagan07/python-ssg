import unittest

from markdown_blocks import markdown_to_blocks


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
