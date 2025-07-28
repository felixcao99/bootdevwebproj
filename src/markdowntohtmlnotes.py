from markdowntoblocks import *
from blocktohtmlnodes import *

def markdown_to_html_node(markdown):
    children_nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        match block_to_block_type(block):
            case BlockType.PARAGRAPH:
                children_nodes.append(paragraphblock_to_htmlnode(block))
            case BlockType.HEADING:
                children_nodes.append(headingblock_to_htmlnode(block))
            case BlockType.CODE:
                children_nodes.append(codeblock_to_htmlnode(block))
            case BlockType.QUOTE:
                children_nodes.append(quoteblock_to_htmlnode(block))
            case BlockType.ULIST:
                children_nodes.append(ulistblock_to_htmlnode(block))
            case BlockType.OLIST:
                children_nodes.append(olistblock_to_htmlnode(block))
            case _:
                raise ValueError(f"Unknown block type for block: {block}")
    return ParentNode("div", children_nodes)


 