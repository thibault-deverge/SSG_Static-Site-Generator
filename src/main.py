from src.enums import TextType
from src.textnode import TextNode, TextType
from src.utils.splitters import split_nodes_link


def main():
    node2 = TextNode(
        "[link](https://i.imgur.com/zjjcJKZ.png) and text ",
        TextType.TEXT,
    )
    new_nodes2 = split_nodes_link([node2])
    print(new_nodes2)
    print("------------------------------")


if __name__ == "__main__":
    main()
