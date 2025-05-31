from src.textnode import TextNode, TextType
from src.htmlnode import HTMLNode, ParentNode, LeafNode
from src.utils import split_nodes_delimiter


def main():
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    print(new_nodes)

    node2 = TextNode("This is `text` with a `code block` word", TextType.TEXT)
    new_nodes2 = split_nodes_delimiter([node2], "`", TextType.CODE)
    print(new_nodes2)

    # node3 = TextNode("This is `text with a `code block` word", TextType.TEXT)
    # new_nodes3 = split_nodes_delimiter([node3], "`", TextType.CODE)
    # print(new_nodes3)

    # node4 = TextNode("Unmatched **bold", TextType.TEXT)
    # new_nodes4 = split_nodes_delimiter([node4], "**", TextType.BOLD)
    # print(new_nodes4)


if __name__ == "__main__":
    main()
