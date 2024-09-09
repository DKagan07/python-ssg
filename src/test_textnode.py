"""this module tests our text nodes"""

import unittest

from textnode import TextNode


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


if __name__ == "__main__":
    unittest.main()
