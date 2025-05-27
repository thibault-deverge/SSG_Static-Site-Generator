from textnode import TextNode, TextType


def main():
    test = TextNode("This is some anchor text", TextType.LINK, "http://boot.dev.com")
    test2 = TextNode("This is some anchor text", TextType.LINK, "http://boot.dev.com")
    print(test == test2)


if __name__ == "__main__":
    main()
