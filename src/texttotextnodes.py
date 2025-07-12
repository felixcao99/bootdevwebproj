from textnode import *
from splitnotes import *

def text_to_text_nodes(text):
    if not text:
        return []
    nodes = []
    input_nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(input_nodes, '**', TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, '_', TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
