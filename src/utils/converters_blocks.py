from src.htmlnode import HTMLNode


def markdown_to_blocks(markdown: str) -> list[str]:
    block_list = []

    for block in markdown.split("\n\n"):
        stripped_block = block.strip()
        if stripped_block != "":
            block_list.append(stripped_block)

    return block_list


def markdown_to_html_node(markdown):
    pass
