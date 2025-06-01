import unittest
from src.enums import TextType
from src.textnode import TextNode
from src.utils.converters_textnode import text_to_textnodes


class TestTextToTextnodes(unittest.TestCase):
    def assert_nodes_equal(self, actual, expected):
        """
        Aide pour comparer deux listes de TextNode sans répéter systématiquement TextNode(...).
        """
        self.assertEqual(
            len(actual), len(expected), msg=f"Length differs: {actual} vs {expected}"
        )
        for a, e in zip(actual, expected):
            self.assertEqual(a, e, msg=f"Node differs: {a!r} != {e!r}")

    def test_plain_text_only(self):
        text = "Just plain text with no formatting."
        nodes = text_to_textnodes(text)
        expected = [TextNode("Just plain text with no formatting.", TextType.TEXT)]
        self.assert_nodes_equal(nodes, expected)

    def test_bold_only(self):
        text = "**hello**"
        nodes = text_to_textnodes(text)
        expected = [TextNode("hello", TextType.BOLD)]
        self.assert_nodes_equal(nodes, expected)

    def test_unmatched_bold_raises(self):
        text = "This is **broken bold"
        with self.assertRaises(Exception):
            _ = text_to_textnodes(text)

    def test_bold_surrounded_text(self):
        text = "a **b** c"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("a ", TextType.TEXT),
            TextNode("b", TextType.BOLD),
            TextNode(" c", TextType.TEXT),
        ]
        self.assert_nodes_equal(nodes, expected)

    def test_italic_only(self):
        text = "_italic_"
        nodes = text_to_textnodes(text)
        expected = [TextNode("italic", TextType.ITALIC)]
        self.assert_nodes_equal(nodes, expected)

    def test_code_only(self):
        text = "`code snippet`"
        nodes = text_to_textnodes(text)
        expected = [TextNode("code snippet", TextType.CODE)]
        self.assert_nodes_equal(nodes, expected)

    def test_image_only(self):
        text = "![alt text](http://example.com/img.png)"
        nodes = text_to_textnodes(text)
        expected = [TextNode("alt text", TextType.IMAGE, "http://example.com/img.png")]
        self.assert_nodes_equal(nodes, expected)

    def test_link_only(self):
        text = "[click here](https://boot.dev)"
        nodes = text_to_textnodes(text)
        expected = [TextNode("click here", TextType.LINK, "https://boot.dev")]
        self.assert_nodes_equal(nodes, expected)

    def test_mixed_inline_features(self):
        text = (
            "This is **text** with an _italic_ word and a `code block` "
            "and an ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        )
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assert_nodes_equal(nodes, expected)

    def test_multiple_images_and_links(self):
        text = "Start ![img1](http://a/1.png) middle ![img2](http://a/2.png) end [L1](http://x) and [L2](http://y)"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("Start ", TextType.TEXT),
            TextNode("img1", TextType.IMAGE, "http://a/1.png"),
            TextNode(" middle ", TextType.TEXT),
            TextNode("img2", TextType.IMAGE, "http://a/2.png"),
            TextNode(" end ", TextType.TEXT),
            TextNode("L1", TextType.LINK, "http://x"),
            TextNode(" and ", TextType.TEXT),
            TextNode("L2", TextType.LINK, "http://y"),
        ]
        self.assert_nodes_equal(nodes, expected)

    def test_bold_link_image_italic_code_sequence(self):
        text = (
            "Start [L](http://x) and **B** then ![I](http://img) " "and _J_ and `K` end"
        )
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("Start ", TextType.TEXT),
            TextNode("L", TextType.LINK, "http://x"),
            TextNode(" and ", TextType.TEXT),
            TextNode("B", TextType.BOLD),
            TextNode(" then ", TextType.TEXT),
            TextNode("I", TextType.IMAGE, "http://img"),
            TextNode(" and ", TextType.TEXT),
            TextNode("J", TextType.ITALIC),
            TextNode(" and ", TextType.TEXT),
            TextNode("K", TextType.CODE),
            TextNode(" end", TextType.TEXT),
        ]
        self.assert_nodes_equal(nodes, expected)

    def test_italic_code_link_image_mixture(self):
        text = "Hello _world_ and `code` and [open](http://o) and ![pic](http://p)!"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("Hello ", TextType.TEXT),
            TextNode("world", TextType.ITALIC),
            TextNode(" and ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("open", TextType.LINK, "http://o"),
            TextNode(" and ", TextType.TEXT),
            TextNode("pic", TextType.IMAGE, "http://p"),
            TextNode("!", TextType.TEXT),
        ]
        self.assert_nodes_equal(nodes, expected)

    def test_adjacent_delimiters(self):
        text = "**a****b**"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("a", TextType.BOLD),
            TextNode("b", TextType.BOLD),
        ]
        self.assert_nodes_equal(nodes, expected)
