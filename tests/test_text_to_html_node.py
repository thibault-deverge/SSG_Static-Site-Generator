import unittest

from src.enums import TextType
from src.textnode import TextNode
from src.utils.converters import text_node_to_html_node


class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text_type(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold_type(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")
        self.assertEqual(html_node.to_html(), "<b>This is a bold node</b>")

    def test_italic_type(self):
        node = TextNode("This is a italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a italic node")
        self.assertEqual(html_node.to_html(), "<i>This is a italic node</i>")

    def test_code_type(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")
        self.assertEqual(html_node.to_html(), "<code>This is a code node</code>")

    def test_link_type(self):
        node = TextNode("This is a link node", TextType.LINK, "http://testurl.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {"href": "http://testurl.com"})
        self.assertEqual(
            html_node.to_html(), '<a href="http://testurl.com">This is a link node</a>'
        )

    def test_img_type(self):
        node = TextNode(
            "This is a img alt", TextType.IMAGE, "http://testsrcimg.jpg.com"
        )
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"alt": "This is a img alt", "src": "http://testsrcimg.jpg.com"},
        )
        self.assertEqual(
            html_node.to_html(),
            '<img alt="This is a img alt" src="http://testsrcimg.jpg.com" />',
        )
