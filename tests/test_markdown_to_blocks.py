import unittest

from src.utils.converters_blocks import markdown_to_blocks


class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_basic_two_paragraphs(self):
        md = "Para 1\n\nPara 2"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Para 1", "Para 2"])

    def test_leading_and_trailing_blank_lines(self):
        md = "\n\n\nFirst paragraph\n\nSecond paragraph\n\n\n"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["First paragraph", "Second paragraph"])

    def test_multiple_consecutive_blank_lines(self):
        md = "A\n\n\n\nB\n\n\nC"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["A", "B", "C"])

    def test_no_double_newline_returns_single_block(self):
        md = "Just one paragraph\nwith a newline\nbut no blank line"
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks, ["Just one paragraph\nwith a newline\nbut no blank line"]
        )

    def test_only_whitespace_returns_empty_list(self):
        md = "   \n  \n\n   \n"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_embedded_list_and_paragraphs(self):
        md = (
            "Title\n\n"
            "- item 1\n"
            "- item 2\n\n\n"
            "Final paragraph\nwith two lines\n\n"
            "End"
        )
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "Title",
                "- item 1\n- item 2",
                "Final paragraph\nwith two lines",
                "End",
            ],
        )

    def test_paragraphs_with_trailing_spaces(self):
        md = "Para one   \n\n   Para two  "
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Para one", "Para two"])

    def test_block_with_only_blank_line_inside(self):
        md = "A\n \nB\n\nC"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["A\n \nB", "C"])

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
