from src.utils.converters import block_to_block_type


def main():
    #     test_markdown = """
    # # This is a heading

    # This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

    # - This is the first list item in a list block
    # - This is a list item
    # - This is another list item
    # """

    #     result = markdown_to_blocks(test_markdown)
    #     print(result)

    test_heading = ""

    result = block_to_block_type(test_heading)
    print(result)


if __name__ == "__main__":
    main()
