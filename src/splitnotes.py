from textnode import *
from extractmarkdown import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if not old_nodes:
        return []
    new_nodes = []
    l = len(delimiter)
    for node in old_nodes:
        if isinstance(node, TextNode):
            if node.text_type == TextType.TEXT:
                pos1 = node.text.find(delimiter)
                if pos1 == -1:
                    new_nodes.append(node)
                else:
                    text1 = node.text[:pos1]
                    if len(text1) > 0:
                        node_left = TextNode(text1, TextType.TEXT)
                        new_nodes.append(node_left)
                    temp_text = node.text[pos1 + l:]
                    pos2 = temp_text.find(delimiter)
                    text2 = temp_text[:pos2]
                    text3 = temp_text[pos2 + l:]
                    node_mid = TextNode(text2, text_type)
                    new_nodes.append(node_mid)
                    if len(text3) > 0:
                        node_right = TextNode(text3, TextType.TEXT)
                        new_nodes.append(node_right)
            else:
                new_nodes.append(node)
    return new_nodes


def split_nodes_image(old_nodes):
    if not old_nodes:
        return []
    new_nodes = []
    for node in old_nodes:
        if isinstance(node, TextNode):
            if node.text_type == TextType.TEXT:
                images = extract_markdown_images(node.text)
                if not images:
                    new_nodes.append(node)
                else:
                    pos_start = 0
                    for image in images:
                        image_text = image[0]
                        image_url = image[1]
                        pos_end = node.text.find("![" + image_text + "]")
                        text = node.text[pos_start:pos_end]
                        if text:
                            new_nodes.append(TextNode(text, TextType.TEXT))
                        new_nodes.append(TextNode(image_text, TextType.IMAGE, url=image_url))
                        pos_start = pos_end + len("![" + image_text + "](" + image_url + ")")
                    if pos_start < len(node.text):
                        new_nodes.append(TextNode(node.text[pos_start:], TextType.TEXT))
            else:
                new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes):
    if not old_nodes:
        return []
    new_nodes = []
    for node in old_nodes:
        if isinstance(node, TextNode):
            if node.text_type == TextType.TEXT:
                links = extract_markdown_links(node.text)
                if not links:
                    new_nodes.append(node)
                else:
                    pos_start = 0
                    for link in links:
                        link_text = link[0]
                        link_url = link[1]
                        pos_end = node.text.find("[" + link_text + "]")
                        text = node.text[pos_start:pos_end]
                        if text:
                            new_nodes.append(TextNode(text, TextType.TEXT))
                        new_nodes.append(TextNode(link_text, TextType.LINK, url=link_url))
                        pos_start = pos_end + len("[" + link_text + "](" + link_url + ")")
                    if pos_start < len(node.text):
                        new_nodes.append(TextNode(node.text[pos_start:], TextType.TEXT))
            else:
                new_nodes.append(node)
    return new_nodes                    
           