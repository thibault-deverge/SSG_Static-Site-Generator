import re

from src.enums import TextType, BlockType
from src.textnode import TextNode
from src.htmlnode import LeafNode
from src.utils.splitters import (
    split_nodes_image,
    split_nodes_link,
    split_nodes_delimiter,
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


def markdown_to_blocks(markdown: str) -> list[str]:
    block_list = []

    for block in markdown.split("\n\n"):
        stripped_block = block.strip()
        if stripped_block != "":
            block_list.append(stripped_block)

    return block_list


PATTERN_HEADING = r"^#{1,6} "
PATTERN_CODE = re.compile(r"^```[\s\S]*?```$", re.DOTALL)
PATTERN_QUOTE = re.compile(r"^(?:>.*(?:\n|$))+$")
PATTERN_UL = re.compile(r"^(?:- .*(?:\n|$))+$")
PATTERN_OL = re.compile(r"^(\d+)\. (.+)$")


def block_to_block_type(markdown_block: str) -> BlockType:
    if re.match(PATTERN_HEADING, markdown_block):
        return BlockType.HEADING
    elif re.match(PATTERN_CODE, markdown_block):
        return BlockType.CODE
    elif re.match(PATTERN_QUOTE, markdown_block):
        return BlockType.QUOTE
    elif re.match(PATTERN_UL, markdown_block):
        return BlockType.UNORDERED_LIST
    else:
        lines = markdown_block.splitlines()

        if len(lines) == 0:
            return BlockType.PARAGRAPH

        for idx, line in enumerate(lines, start=1):
            match = re.match(PATTERN_OL, line)
            if not match:
                return BlockType.PARAGRAPH
            num = int(match.group(1))
            if num != idx:
                return BlockType.PARAGRAPH

        return BlockType.ORDERED_LIST
