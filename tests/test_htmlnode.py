import unittest

from src.htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_all_default_value(self):
        node = HTMLNode()
        assert node.tag == None
        assert node.value == None
        assert node.children == None
        assert node.props == None

    def test_repr_shows_all_fields(self):
        node = HTMLNode("div", "hello", [], {"class": "foo"})
        assert repr(node) == "HTMLNode(div, hello, [], {'class': 'foo'})"

    def test_repr_with_none_fields(self):
        node = HTMLNode("div", "hello", props={"class": "foo"})
        assert repr(node) == "HTMLNode(div, hello, None, {'class': 'foo'})"

    def test_props_to_html_single(self):
        node = HTMLNode("div", "hello", [], {"class": "foo"})
        self.assertEqual(node.props_to_html(), 'class="foo"')

    def test_props_to_html_multi(self):
        node = HTMLNode("div", "hello", [], {"a": "1", "b": "2"})
        self.assertEqual(node.props_to_html(), 'a="1" b="2"')

    def test_eq_identical_nodes(self):
        child = HTMLNode("span", "x", [], {"data": "1"})
        a = HTMLNode("div", None, [child], {"class": "c"})
        b = HTMLNode("div", None, [child], {"class": "c"})
        assert a == b

    def test_eq_different_node(self):
        child = HTMLNode("span", "x", [], {"data": "1"})
        a = HTMLNode("div", None, [child], {"class": "c"})
        b = HTMLNode("div", None, [child], {"class": "dddddd"})
        assert a != b

    def test_eq_other_type_is_not_HTMLNode(self):
        node = HTMLNode("div")
        assert not (node == "not-a-node")
