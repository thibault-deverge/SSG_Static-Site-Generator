from src.textnode import TextType, TextNode
from src.htmlnode import LeafNode


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


def split_nodes_delimiter(
    old_nodes: list["TextNode"], delimiter: str, text_type: TextType
) -> list:
    new_node = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_node.append(old_node)
        else:
            split_node = old_node.text.split(delimiter)

            if len(split_node) % 2 == 0:
                raise Exception("invalid markdown syntax, no delimiter found.")

            for i in range(0, len(split_node)):
                if i % 2 == 0 and split_node[i] != "":
                    new_node.append(TextNode(split_node[i], TextType.TEXT))
                elif split_node[i] != "":
                    new_node.append(TextNode(split_node[i], text_type))

    return new_node
