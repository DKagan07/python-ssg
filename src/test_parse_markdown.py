import unittest

from parse_markdown import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_with_delimiter,
)
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


class TestExtractMDImages(unittest.TestCase):
    def test_extract_md_images(self):
        img_text = (
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) image"
        )

        result = extract_markdown_images(img_text)
        self.assertListEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif")], result)

    def test_extract_mult_images(self):
        img_text = "This is text with multiple images, including ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"

        result = extract_markdown_images(img_text)
        self.assertListEqual(
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
            result,
        )

    def test_extract_img_no_alt(self):
        img_text = (
            "This is an image with no alt text ![](https://i.imgur.com/aKaOqIh.gif)"
        )

        result = extract_markdown_images(img_text)

        self.assertListEqual([("", "https://i.imgur.com/aKaOqIh.gif")], result)


class TestExtractMDLinks(unittest.TestCase):
    def test_extract_links(self):
        link_text = "This is text with a link [to boot dev](https://www.boot.dev)"

        result = extract_markdown_links(link_text)

        self.assertListEqual([("to boot dev", "https://www.boot.dev")], result)

    def test_multi_image_extract_links(self):
        link_text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"

        result = extract_markdown_links(link_text)

        self.assertListEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
            result,
        )

    def test_image_extract_no_anchor_text(self):
        link_text = "This is text with a link [](https://www.boot.dev)"

        result = extract_markdown_links(link_text)

        self.assertListEqual([("", "https://www.boot.dev")], result)
