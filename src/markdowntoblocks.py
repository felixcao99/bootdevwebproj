from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = []
    final_blocks = []
    if not markdown:
        return blocks
    blocks = markdown.split("\n\n")
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        else:
            final_blocks.append(block)
    return final_blocks

def block_to_block_type(block):
    pattern_heading = r"^#{1,6} "
    pattern_code_start = r"^```"
    pattern_code_end = r"```$"
    pattern_quote = r"^> "
    pattern_ulist = r"^- "
    pattern_olist = r"^\d+\. "
    if re.match(pattern_heading, block):
        return BlockType.HEADING
    elif re.match(pattern_code_start, block) and re.search(pattern_code_end, block):
        return BlockType.CODE
    elif re.match(pattern_quote, block):
        return BlockType.QUOTE
    elif re.match(pattern_ulist, block):
        return BlockType.ULIST
    elif re.match(pattern_olist, block):
        return BlockType.OLIST
    else:
        return BlockType.PARAGRAPH

