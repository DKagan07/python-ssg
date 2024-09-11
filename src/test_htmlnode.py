"""this module tests our html nodes"""

import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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
        result = ""

        self.assertEqual(hnode.props_to_html(), result)


class TestLeafNode(unittest.TestCase):
    """test leaf node"""

    def test_to_html_anchor(self):
        """test to_html with an anchor"""

        value = "Value here!"
        tag = "a"
        url = "https://www.google.com"
        result = '<a href="https://www.google.com">Value here!</a>'
        ln = LeafNode(tag, value, {"href": url})

        self.assertEqual(ln.to_html(), result)

    def test_to_html_div(self):
        """test to_html with a div"""

        value = "inner div"
        tag = "div"
        props = {"class": "header1"}
        result = '<div class="header1">inner div</div>'
        ln = LeafNode(tag, value, props)

        self.assertEqual(ln.to_html(), result)

    def test_to_html_div_no_props(self):
        """test to_html with a div without props"""

        value = "inner div"
        tag = "div"
        result = "<div>inner div</div>"
        ln = LeafNode(tag, value)

        self.assertEqual(ln.to_html(), result)

    def test_to_html_no_value(self):
        """test to_html without a value"""

        tag = "div"
        props = {"class": "header1"}
        ln = LeafNode(tag, None, props)

        with self.assertRaises(ValueError):
            ln.to_html()

    def test_to_html_no_tag(self):
        """test to_html without a tag"""
        value = "hello world"
        result = "hello world"
        ln = LeafNode(None, value)

        self.assertEqual(ln.to_html(), result)


class TestParentNode(unittest.TestCase):
    def test_happy_to_html(self):
        """tests happy path for parent to_html"""

        test_children = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ]
        result = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        pn = ParentNode("p", test_children, None)

        self.assertEqual(pn.to_html(), result)

    def test_nested_to_html(self):
        """test nested parent in to_html"""

        test_inner_parent = ParentNode("p", [LeafNode("b", "Bold inner text")])
        test_children = [test_inner_parent]

        result = "<div><p><b>Bold inner text</b></p></div>"
        pn = ParentNode("div", test_children, None)

        self.assertEqual(pn.to_html(), result)

    def test_missing_tag(self):
        """tests top parent missing tag"""

        test_children = [LeafNode("b", "Bold text")]

        pn = ParentNode(None, test_children, None)
        with self.assertRaises(ValueError):
            pn.to_html()

    def test_missing_tag_in_child_parent(self):
        """test nested parent missing tag"""

        test_inner_parent = ParentNode(None, [LeafNode("b", "Bold inner text")])
        test_children = [test_inner_parent]

        pn = ParentNode("div", test_children, None)
        with self.assertRaises(ValueError):
            pn.to_html()

    def test_missing_children(self):
        """test missing child parameter"""

        pn = ParentNode("p", None, None)

        with self.assertRaises(ValueError):
            pn.to_html()

    def test_missing_children_in_child_parent(self):
        """test missing child parameter in nested parent"""

        test_inner_parent = ParentNode("p", None)
        test_children = [test_inner_parent]

        pn = ParentNode("div", test_children, None)
        with self.assertRaises(ValueError):
            pn.to_html()


if __name__ == "__main__":
    unittest.main()
