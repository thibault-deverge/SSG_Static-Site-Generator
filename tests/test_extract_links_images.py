import unittest

from src.utils.extracters import extract_markdown_images, extract_markdown_links


class TestSplitNodesDelimiter(unittest.TestCase):
    # --- EXTRACT IMAGES ---
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_multiple(self):
        text = (
            "First ![img1](http://a.com/1.png) and second ![img2](https://b.org/2.jpg)"
        )
        expected = [
            ("img1", "http://a.com/1.png"),
            ("img2", "https://b.org/2.jpg"),
        ]
        self.assertListEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_images_empty_alt(self):
        text = "Here is an image with no alt: ![](http://example.com/x.png)"
        self.assertListEqual(
            extract_markdown_images(text), [("", "http://example.com/x.png")]
        )

    def test_extract_markdown_images_url_with_parentheses(self):
        text = "![test](http://example.com/path_(1).png)"
        self.assertNotEqual(
            extract_markdown_images(text), [("test", "http://example.com/path_(1).png")]
        )
        self.assertListEqual(extract_markdown_images(text), [])

    def test_extract_markdown_images_no_match(self):
        text = "No markdown images here!"
        self.assertListEqual(extract_markdown_images(text), [])

    #  --- EXTRACT LINKS ---
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
            matches,
        )

    def test_extract_markdown_links_multiple(self):
        text = "One [first](http://a/1) and [second](https://b/2) link."
        expected = [("first", "http://a/1"), ("second", "https://b/2")]
        self.assertListEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_links_not_image(self):
        text = "![alt](http://img) and [link](http://url)"
        self.assertListEqual(extract_markdown_links(text), [("link", "http://url")])

    def test_extract_markdown_links_empty_text(self):
        text = "Link sans texte visible: [](http://nolabel)"
        self.assertListEqual(extract_markdown_links(text), [("", "http://nolabel")])

    def test_extract_markdown_links_nested_brackets(self):
        text = "A [bad [nested]](http://x) example"
        self.assertListEqual(extract_markdown_links(text), [])

    def test_extract_markdown_links_no_match(self):
        text = "Just plain text, nothing to see."
        self.assertListEqual(extract_markdown_links(text), [])
