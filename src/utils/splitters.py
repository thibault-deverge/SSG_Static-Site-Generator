from src.enums import TextType
from src.textnode import TextNode
from src.utils.extracters import extract_markdown_images, extract_markdown_links


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


def split_nodes_image(old_nodes):
    new_node = []

    for old_node in old_nodes:
        matches = extract_markdown_images(old_node.text)
        if len(matches) == 0:
            new_node.append(old_node)
        else:
            old_text_copy = old_node.text

            for match in matches:
                split = old_text_copy.split(f"![{match[0]}]({match[1]})", 1)
                if split[0] == "":
                    new_node.append(TextNode(match[0], TextType.IMAGE, match[1]))
                else:
                    new_node.append(TextNode(split[0], TextType.TEXT))
                    new_node.append(TextNode(match[0], TextType.IMAGE, match[1]))
                    pass
                old_text_copy = split[1]

            if old_text_copy != "":
                new_node.append(TextNode(old_text_copy, TextType.TEXT))

    return new_node


def split_nodes_link(old_nodes):
    new_node = []

    for old_node in old_nodes:
        matches = extract_markdown_links(old_node.text)
        if len(matches) == 0:
            new_node.append(old_node)
        else:
            old_text_copy = old_node.text

            for match in matches:
                split = old_text_copy.split(f"[{match[0]}]({match[1]})", 1)
                if split[0] == "":
                    new_node.append(TextNode(match[0], TextType.LINK, match[1]))
                else:
                    new_node.append(TextNode(split[0], TextType.TEXT))
                    new_node.append(TextNode(match[0], TextType.LINK, match[1]))
                    pass
                old_text_copy = split[1]

            if old_text_copy != "":
                new_node.append(TextNode(old_text_copy, TextType.TEXT))

    return new_node
