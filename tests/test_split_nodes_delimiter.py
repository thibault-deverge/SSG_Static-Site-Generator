import unittest

from src.enums import TextType
from src.textnode import TextNode
from src.utils.splitters import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_simple_one_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT, None),
                TextNode("code block", TextType.CODE, None),
                TextNode(" word", TextType.TEXT, None),
            ],
        )

    def test_simple_one_delimiter_italic(self):
        node = TextNode("This is text with a *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT, None),
                TextNode("italic", TextType.ITALIC, None),
                TextNode(" word", TextType.TEXT, None),
            ],
        )

    def test_simple_one_delimiter_italic(self):
        node = TextNode("This is text with a *italic* word", TextType.TEXT)
        node2 = TextNode("This is another text with a *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node, node2], "*", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT, None),
                TextNode("italic", TextType.ITALIC, None),
                TextNode(" word", TextType.TEXT, None),
                TextNode("This is another text with a ", TextType.TEXT, None),
                TextNode("italic", TextType.ITALIC, None),
                TextNode(" word", TextType.TEXT, None),
            ],
        )

    def test_two_delimiters_bold(self):
        node = TextNode(
            "This is text with a **bold** word and **another one** more", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT, None),
                TextNode("bold", TextType.BOLD, None),
                TextNode(" word and ", TextType.TEXT, None),
                TextNode("another one", TextType.BOLD, None),
                TextNode(" more", TextType.TEXT, None),
            ],
        )

    def test_no_delimiter(self):
        node = TextNode("This is text with no delimiter", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with no delimiter", TextType.TEXT, None),
            ],
        )

    def test_consecutive_delimiter_empty(self):
        node = TextNode(
            "This is text with **** delimiter sticked together", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with ", TextType.TEXT, None),
                TextNode(" delimiter sticked together", TextType.TEXT, None),
            ],
        )

    def test_oldnode_not_text_type(self):
        node = TextNode("This is not a text type node", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is not a text type node", TextType.BOLD, None),
            ],
        )

    def test_delimiter_at_start(self):
        node = TextNode("`code block` at start", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("code block", TextType.CODE, None),
                TextNode(" at start", TextType.TEXT, None),
            ],
        )

    def test_delimiter_at_end(self):
        node = TextNode("delimiter at **end**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("delimiter at ", TextType.TEXT, None),
                TextNode("end", TextType.BOLD, None),
            ],
        )

    def test_single_delimiter_unbalanced(self):
        node = TextNode("delimiter at **end", TextType.TEXT)
        with self.assertRaises(Exception) as cm:
            split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertIn("invalid markdown", str(cm.exception))

    def test_multiple_delimiter_unbalanced(self):
        node = TextNode("delimiter** at **end**", TextType.TEXT)
        with self.assertRaises(Exception) as cm:
            split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertIn("invalid markdown", str(cm.exception))
