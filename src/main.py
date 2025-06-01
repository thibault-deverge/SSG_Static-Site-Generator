from src.enums import TextType
from src.textnode import TextNode, TextType
from src.utils.converters import text_to_textnodes
from src.utils.splitters import split_nodes_link

import pprint


def main():
    test_str = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

    pprint.pp(text_to_textnodes(test_str))


if __name__ == "__main__":
    main()
