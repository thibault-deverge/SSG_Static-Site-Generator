import re

PATTERN_IMAGE = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
PATTERN_LINK = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
PATTERN_H1 = re.compile(r"(?m)^#\s+(.+)$")


def extract_markdown_images(text):
    matches = re.findall(PATTERN_IMAGE, text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(PATTERN_LINK, text)
    return matches


def extract_title(markdown):
    matches = re.findall(PATTERN_H1, markdown.strip())
    if len(matches) != 1:
        raise Exception("Markdown file must have one H1 element")

    return matches[0].strip()
