import unittest

from src.textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("foo", TextType.BOLD)
        node2 = TextNode("foo", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("foo", TextType.BOLD, "http://testurl.com")
        node2 = TextNode("foo", TextType.BOLD, "http://testurl.com")
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("foo", TextType.BOLD)
        node2 = TextNode("foo bar", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_text_type(self):
        node = TextNode("foo", TextType.ITALIC)
        node2 = TextNode("foo ", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_none_vs_empty_url(self):
        node = TextNode("foo", TextType.BOLD)
        node2 = TextNode("foo", TextType.BOLD, "")
        self.assertNotEqual(node, node2)

    def test_repr_without_url(self):
        node = TextNode("foo", TextType.BOLD)
        assert repr(node) == "TextNode(foo, bold, None)"

    def test_repr_with_url(self):
        node = TextNode("foo", TextType.LINK, "http://testurl.com")
        assert repr(node) == "TextNode(foo, link, http://testurl.com)"


if __name__ == "__main__":
    unittest.main()
