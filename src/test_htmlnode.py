"""this module tests our html nodes"""

import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    """test html node"""

    def test_props_to_html_2_props(self):
        """tests a happy path for props_to_html with 2 props"""

        href = "https://www.google.com"
        target = "_blank"
        result = ' href="https://www.google.com" target="_blank"'
        hnode = HTMLNode("a", props={"href": href, "target": target})

        self.assertEqual(hnode.props_to_html(), result)

    def test_props_to_html_1_prop(self):
        """tests a happy path for props_to_html with 1 prop"""

        href = "https://www.google.com"
        result = ' href="https://www.google.com"'
        hnode = HTMLNode("a", props={"href": href})

        self.assertEqual(hnode.props_to_html(), result)

    def test_props_to_html_0_props(self):
        """tests a happy path for props_to_html with 0 props"""

        hnode = HTMLNode("a")
        result = " "

        self.assertEqual(hnode.props_to_html(), result)


if __name__ == "__main__":
    unittest.main()
