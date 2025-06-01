from src.utils.converters_blocks import markdown_to_html_node


def main():
    md1 = """This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here
"""

    node = markdown_to_html_node(md1)

    print("-----------")
    md2 = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
    node2 = markdown_to_html_node(md2)


if __name__ == "__main__":
    main()
