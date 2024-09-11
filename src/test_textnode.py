"""this module tests our text nodes"""

import unittest

from htmlnode import LeafNode
from textnode import TextNode, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    """TestTextNode is the class that will hold our text node unit tests"""

    def test_eq(self):
        """tests if 2 nodes are equal"""
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_url_none(self):
        """tests that if no url is present, it is of type None"""
        node = TextNode("This is a text node", "bold")
        self.assertEqual(node.url, None)

    def test_diff_text_types(self):
        """tests difference in text types"""
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italics")
        self.assertNotEqual(node, node2)

    def test_diff_texts(self):
        """tests different texts"""
        node = TextNode("This is another text node", "bold")
        node2 = TextNode("This is a text node", "italics")
        self.assertNotEqual(node, node2)

    def test_presence_of_url(self):
        """tests the equality of these text nodes with presence of url"""
        node = TextNode("This is text node", "bold", "https://www.google.com")
        node2 = TextNode("This is a text node", "italics")
        self.assertNotEqual(node, node2)


class TestTextToHTMLConversion(unittest.TestCase):
    """testing the text to html node conversion"""

    def test_happy_path(self):
        """testing happy path"""

        test_text = "test bold text"
        tn = TextNode(test_text, "bold")
        ln = text_node_to_html_node(tn)
        result = LeafNode("b", test_text)

        self.assertEqual(ln, result)

    def test_invalid_type(self):
        """testing invalid type in text node"""

        test_text = "test bold text"
        tn = TextNode(test_text, "invalid_type")

        with self.assertRaises(Exception):
            text_node_to_html_node(tn)

    def test_with_props(self):
        """testing conversion with props"""

        url = "https://www.google.com"
        test_text = "test image text"
        test_props = {"href": url, "alt": test_text}

        tn = TextNode(test_text, "image", url)
        ln = text_node_to_html_node(tn)
        result = LeafNode("img", "", test_props)

        self.assertEqual(ln, result)


if __name__ == "__main__":
    unittest.main()
