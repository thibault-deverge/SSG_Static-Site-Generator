import re

from src.enums import BlockType


def block_to_block_type(markdown_block: str) -> BlockType:
    PATTERN_HEADING = r"^#{1,6} "
    PATTERN_CODE = re.compile(r"^```[\s\S]*?```$", re.DOTALL)
    PATTERN_QUOTE = re.compile(r"^(?:>.*(?:\n|$))+$")
    PATTERN_UL = re.compile(r"^(?:- .*(?:\n|$))+$")
    PATTERN_OL = re.compile(r"^(\d+)\. (.+)$")

    if re.match(PATTERN_HEADING, markdown_block):
        return BlockType.HEADING
    elif re.match(PATTERN_CODE, markdown_block):
        return BlockType.CODE
    elif re.match(PATTERN_QUOTE, markdown_block):
        return BlockType.QUOTE
    elif re.match(PATTERN_UL, markdown_block):
        return BlockType.UNORDERED_LIST
    else:
        lines = markdown_block.splitlines()

        if len(lines) == 0:
            return BlockType.PARAGRAPH

        for idx, line in enumerate(lines, start=1):
            match = re.match(PATTERN_OL, line)
            if not match:
                return BlockType.PARAGRAPH
            num = int(match.group(1))
            if num != idx:
                return BlockType.PARAGRAPH

        return BlockType.ORDERED_LIST
