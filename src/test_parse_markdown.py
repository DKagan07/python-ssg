import unittest

from parse_markdown import split_nodes_with_delimiter
from textnode import TextNode


class TestParseMarkdown(unittest.TestCase):
    def test_bold_delim(self):
        node = TextNode("This is a **bold** statement.", "text")

        new_nodes = split_nodes_with_delimiter([node], "**", "bold")
        self.assertListEqual(
            [
                TextNode("This is a ", "text"),
                TextNode("bold", "bold"),
                TextNode(" statement.", "text"),
            ],
            new_nodes,
        )

    def test_multi_bold_delim(self):
        node = TextNode(
            "This is a **bold** and here's **another bolded** word.", "text"
        )

        new_nodes = split_nodes_with_delimiter([node], "**", "bold")
        self.assertListEqual(
            [
                TextNode("This is a ", "text"),
                TextNode("bold", "bold"),
                TextNode(" and here's ", "text"),
                TextNode("another bolded", "bold"),
                TextNode(" word.", "text"),
            ],
            new_nodes,
        )

    def test_italics_delim(self):
        node = TextNode("This is a *italic* statement.", "text")

        new_nodes = split_nodes_with_delimiter([node], "*", "italic")
        self.assertListEqual(
            [
                TextNode("This is a ", "text"),
                TextNode("italic", "italic"),
                TextNode(" statement.", "text"),
            ],
            new_nodes,
        )

    def test_multi_italic_delim(self):
        node = TextNode("This is a *italic* and here's *another italic* word.", "text")

        new_nodes = split_nodes_with_delimiter([node], "*", "italic")
        self.assertListEqual(
            [
                TextNode("This is a ", "text"),
                TextNode("italic", "italic"),
                TextNode(" and here's ", "text"),
                TextNode("another italic", "italic"),
                TextNode(" word.", "text"),
            ],
            new_nodes,
        )

    def test_raised_exception(self):
        node = TextNode("This is a *italic and here's *another italic* word.", "text")

        with self.assertRaises(ValueError):
            split_nodes_with_delimiter([node], "*", "italic")
