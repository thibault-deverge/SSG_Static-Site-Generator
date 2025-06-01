from enum import Enum


class TextType(Enum):
    """Inline text kinds for Markdown-to-HTML rendering."""

    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
