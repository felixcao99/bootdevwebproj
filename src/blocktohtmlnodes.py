from texttotextnodes import *
from textnotetohtmlnode import *
from leafnode import *

def text_to_children(text):
    if not text:
        return []
    nodes = text_to_text_nodes(text)
    leafnodes = []
    for textnote in nodes:
        leafnode = text_node_to_html_node(textnote)
        if leafnode:
            leafnodes.append(leafnode)
    return leafnodes

def paragraphblock_to_htmlnode(paragraph):
    lines = paragraph.split('\n')
    leafnodes = []
    newline = LeafNode("","<br>")
    for i in range(len(lines)):
        linetext = lines[i].strip()
        if linetext:
            children = text_to_children(linetext)
            if children:
                leafnodes.extend(children) 
        else:
            continue
        if i < len(lines) - 1:
            leafnodes.append(newline)
    paragraph_node = ParentNode("p", leafnodes)
    # return paragraph_node.to_html()
    return paragraph_node

def headingblock_to_htmlnode(heading):
    match heading.count('#'):
        case 1:
            tag = "h1"
        case 2:
            tag = "h2"
        case 3:
            tag = "h3"
        case 4:
            tag = "h4"
        case 5:
            tag = "h5"
        case 6:
            tag = "h6"
        case _:
            raise ValueError("Invalid heading level")
    content = heading.strip('#').strip()
    if not content:
        raise ValueError("Heading cannot be empty")
    children = text_to_children(content)
    if len(children) > 1:
        return ParentNode(tag, children)
    else:
        return LeafNode(tag, content)

def codeblock_to_htmlnode(code):
    code = code.strip('`')
    return LeafNode("code", code)

# def quoteblock_to_htmlnode(quote):
#     quote = quote.strip('>')
#     return LeafNode("blockquote", quote)

def quoteblock_to_htmlnode(quote):
    lines = quote.split('\n')
    leafnodes = []
    newline = LeafNode("","<br>")
    for i in range(len(lines)):
        linetext = lines[i].strip(">").strip()
        if linetext:
            children = text_to_children(linetext)
            if children:
                leafnodes.extend(children) 
        else:
            continue
        if i < len(lines) - 1:
            leafnodes.append(newline)
    paragraph_node = ParentNode("blockquote", leafnodes)
    return paragraph_node


def ulistblock_to_htmlnode(list):
    tag = 'ul'
    list_items = []
    lines = list.split('\n')
    for line in lines:
        content = line.strip("-").strip()
        if not content:
            raise ValueError("Heading cannot be empty")
        children = text_to_children(content)
        if len(children) > 0:
            list_items.append(ParentNode("li", children))
        else:
            list_items.append(LeafNode("li", content))
    return ParentNode(tag, list_items)

def olistblock_to_htmlnode(list):
    tag = 'ol'
    list_items = []
    lines = list.split('\n')
    for line in lines:
        content = line.strip()
        pos = content.find('.')
        content = content[pos + 1:].strip()
        if not content:
            raise ValueError("Heading cannot be empty")
        children = text_to_children(content)
        if len(children) > 0:
            list_items.append(ParentNode("li", children))
        else:
            list_items.append(LeafNode("li", content))
    return ParentNode(tag, list_items)

# paragraph = """This is a paragraph with some text.
# It has multiple lines.      
# This is the second line.
# test **bold** and _italic_ and `code` text.
# This is text with a link [to boot dev](https://www.boot.dev) and an ![image](https://i.imgur.com/zjjcJKZ.png)"""
# print(paragraphblock_to_htmlnode(paragraph).to_html())

# heading = "# This is text with a link [to boot dev](https://www.boot.dev)"
# print(headingblock_to_htmlnode(heading).to_html())

# heading = "### This is text with a link"
# print(headingblock_to_htmlnode(heading).to_html())

# ulist = """- Item 1
# - Item 2
# - Item 3
# - Item 4 and a link [to boot dev](https://www.boot.dev)"""
# ulist_node = ulistblock_to_htmlnode(ulist)
# print(ulist_node.to_html())

# olist = """1. First item
# 2. Second item
# 3. Third item
# 4. Item 4 and a link [to boot dev](https://www.boot.dev)"""
# olist_node = olistblock_to_htmlnode(olist)
# print(olist_node.to_html())
