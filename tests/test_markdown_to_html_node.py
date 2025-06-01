import unittest
import textwrap

from src.enums import BlockType
from src.htmlnode import ParentNode, LeafNode
from src.utils.converters_blocks import (
    markdown_to_html_node,
)


class TestMarkdownToHtmlBlock(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )


def test_codeblock(self):
    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )


def test_heading(self):
    md = textwrap.dedent(
        """
    # My Heading

    """
    )
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(html, "<div><h1>My Heading</h1></div>")


def test_unordered_list(self):
    md = textwrap.dedent(
        """
    - First item
    - Second item
    - Third item

    """
    )
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><ul><li>First item</li><li>Second item</li><li>Third item</li></ul></div>",
    )


def test_paragraphs(self):
    md = textwrap.dedent(
        """
            This is **bolded** paragraph
            text in a p
            tag here

            This is another paragraph with _italic_ text and `code` here

        """
    )
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div>"
        "<p>This is <b>bolded</b> paragraph text in a p tag here</p>"
        "<p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p>"
        "</div>",
    )


def test_codeblock(self):
    md = textwrap.dedent(
        """
        ```
        This is text that _should_ remain
        the **same** even with inline stuff
        ```
    """
    )
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div>"
        "<pre><code>"
        "This is text that _should_ remain\nthe **same** even with inline stuff\n"
        "</code></pre>"
        "</div>",
    )


def test_ordered_list(self):
    md = textwrap.dedent(
        """
        1. First
        2. Second
        3. Third

    """
    )
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div>" "<ol><li>First</li><li>Second</li><li>Third</li></ol>" "</div>",
    )


def test_quote_block(self):
    md = textwrap.dedent(
        """
        > This is a quote
        > spanning two lines
        > in the same block

    """
    )
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div>"
        "<blockquote>This is a quote spanning two lines in the same block</blockquote>"
        "</div>",
    )


def test_mixed_heading_and_list(self):
    md = textwrap.dedent(
        """
        ## Shopping List

        - Apples
        - Bananas

        """
    )
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div>"
        "<h2>Shopping List</h2>"
        "<ul><li>Apples</li><li>Bananas</li></ul>"
        "</div>",
    )
