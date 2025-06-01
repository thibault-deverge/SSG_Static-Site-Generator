import unittest
from src.enums import BlockType
from src.utils.converters_type import block_to_block_type


class TestTextToTextnodes(unittest.TestCase):
    def test_heading_level_1(self):
        markdown = "# Title of section"
        self.assertEqual(block_to_block_type(markdown), BlockType.HEADING)

    def test_heading_level_3(self):
        markdown = "### Subsection header"
        self.assertEqual(block_to_block_type(markdown), BlockType.HEADING)

    def test_not_a_heading(self):
        markdown = "#####"
        self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)

    def test_not_a_heading(self):
        markdown = "####### too much"
        self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)

    def test_code_block_exact(self):
        markdown = "```python\nprint('hello')\n```"
        self.assertEqual(block_to_block_type(markdown), BlockType.CODE)

    def test_code_block_not_closed(self):
        markdown = "```js\nconsole.log('oops')"
        self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)

    def test_quote_simple(self):
        markdown = "> Ceci est une citation"
        self.assertEqual(block_to_block_type(markdown), BlockType.QUOTE)

    def test_quote_multiline(self):
        markdown = "> L1\n> L2\n> L3"
        self.assertEqual(block_to_block_type(markdown), BlockType.QUOTE)

    def test_quote_multiline2(self):
        markdown = "> Texte indenté\n> another line"
        self.assertEqual(block_to_block_type(markdown), BlockType.QUOTE)

    def test_not_quote_mixed(self):
        markdown = "> Bon\nPas une citation"
        self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)

    def test_unordered_list_dash(self):
        markdown = "- item 1\n- item 2\n- item 3"
        self.assertEqual(block_to_block_type(markdown), BlockType.UNORDERED_LIST)

    def test_not_unordered_list_plus(self):
        markdown = "+ choix A\n+ choix B"
        self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)

    def test_not_unordered_list_star(self):
        markdown = "* puce 1\n* puce 2"
        self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)

    def test_not_unordered_list(self):
        markdown = "-item sans espace"
        self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)

    def test_ordered_list_valid(self):
        markdown = "1. premier\n2. deuxième\n3. troisième"
        self.assertEqual(block_to_block_type(markdown), BlockType.ORDERED_LIST)

    def test_ordered_list_single_line(self):
        markdown = "1. seul élément"
        self.assertEqual(block_to_block_type(markdown), BlockType.ORDERED_LIST)

    def test_ordered_list_wrong_numbering(self):
        markdown = "1. un\n3. deux\n2. trois"
        self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)

    def test_ordered_list_non_numeric_prefix(self):
        markdown = "1) point\n2) second"
        self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)

    def test_mixed_ordered_and_unordered(self):
        markdown = "1. un\n- deux\n2. trois"
        self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)

    def test_empty_block(self):
        markdown = ""
        self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)

    def test_whitespace_block(self):
        markdown = "   \n  "
        self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)

    def test_heading_precedence_over_list(self):
        markdown = "# 1. Ceci n’est pas une liste ordonnée"
        self.assertEqual(block_to_block_type(markdown), BlockType.HEADING)

    def test_code_precedence_over_quote(self):
        markdown = "```js\n> ceci n’est pas une citation\n```"
        self.assertEqual(block_to_block_type(markdown), BlockType.CODE)

    def test_quote_precedence_over_unordered_list(self):
        markdown = "> - faux item\n> - faux item2"
        self.assertEqual(block_to_block_type(markdown), BlockType.QUOTE)

    def test_unordered_precedence_over_paragraph(self):
        markdown = "-item sans espace"
        self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)
