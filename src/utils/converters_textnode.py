from src.enums import TextType
from src.textnode import TextNode
from src.htmlnode import LeafNode
from src.utils.splitters import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
)


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, props={"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode(
                "img", "", props={"alt": text_node.text, "src": text_node.url}
            )
        case _:
            raise Exception("Text node should have a valid text type")


def text_to_textnodes(text: str) -> list:
    text_node = TextNode(text, TextType.TEXT)

    splitted_link = split_nodes_link([text_node])
    splitted_image = split_nodes_image([*splitted_link])
    splitted_bold = split_nodes_delimiter([*splitted_image], "**", TextType.BOLD)
    splitted_italic = split_nodes_delimiter([*splitted_bold], "_", TextType.ITALIC)
    splitted_code = split_nodes_delimiter([*splitted_italic], "`", TextType.CODE)

    return splitted_code
