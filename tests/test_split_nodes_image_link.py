import unittest

from src.enums import TextType
from src.textnode import TextNode
from src.utils.splitters import split_nodes_image, split_nodes_link


class TestSplitImageLink(unittest.TestCase):
    # ------ IMAGES ------
    def test_split_two_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_two_images_sticked(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png)![image2](https://i.imgurrtrr.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(
                    "image2", TextType.IMAGE, "https://i.imgurrtrr.com/zjjcJKZ.png"
                ),
            ],
            new_nodes,
        )

    def test_split_only_image(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_then_text(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) and text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and text", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_text_then_image(self):
        node = TextNode(
            "text and ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("text and ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_two_images_begin_and_end(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image",
                    TextType.IMAGE,
                    "https://i.imgur.com/3elNhQu.png",
                ),
            ],
            new_nodes,
        )

    # ------ LINKS ------
    def test_split_two_links(self):
        node = TextNode(
            "This is text with an [link](https://link.com/) and another [second link](https://secondlink.com/)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://link.com/"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://secondlink.com/"),
            ],
            new_nodes,
        )

    def test_split_two_link_sticked(self):
        node = TextNode(
            "[link](https://test1.com/)[link2](https://test2.com/)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link", TextType.LINK, "https://test1.com/"),
                TextNode("link2", TextType.LINK, "https://test2.com/"),
            ],
            new_nodes,
        )

    def test_split_only_link(self):
        node = TextNode(
            "[link](https://testlink.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link", TextType.LINK, "https://testlink.com"),
            ],
            new_nodes,
        )

    def test_split_link_then_text(self):
        node = TextNode(
            "[link](https://testlink.com) and text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link", TextType.LINK, "https://testlink.com"),
                TextNode(" and text", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_text_then_link(self):
        node = TextNode(
            "text and [link](https://testlink.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("text and ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://testlink.com"),
            ],
            new_nodes,
        )

    def test_split_two_links_begin_and_end(self):
        node = TextNode(
            "[link1](https://link1.com) and another [link2](https://link2.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link1", TextType.LINK, "https://link1.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "link2",
                    TextType.LINK,
                    "https://link2.com",
                ),
            ],
            new_nodes,
        )
