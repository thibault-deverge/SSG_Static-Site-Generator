import unittest

from src.htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p_no_props(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_p_with_single_props(self):
        node = LeafNode("p", "Hello, world!", {"width": "50px"})
        self.assertEqual(node.to_html(), '<p width="50px">Hello, world!</p>')

    def test_leaf_to_html_p_with_multiple_props(self):
        node = LeafNode("p", "Hello, world!", {"width": "50px", "height": "100px"})
        self.assertEqual(
            node.to_html(), '<p width="50px" height="100px">Hello, world!</p>'
        )
