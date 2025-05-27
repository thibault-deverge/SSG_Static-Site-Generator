from textnode import TextNode, TextType


def main():
    test = TextNode("This is some anchor text", TextType.LINK, "http://boot.dev.com")
    print(test)


if __name__ == "__main__":
    main()
