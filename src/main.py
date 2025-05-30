from textnode import TextNode, TextType
from htmlnode import HTMLNode

dict = {"alt": "some text on the node", "target": "_blank"}


def main():
    HtmlNodeTest = HTMLNode("p", "Hello world!", None, dict)
    print(f"-{HtmlNodeTest.props_to_html()}-")


if __name__ == "__main__":
    main()
