from htmlnode import *

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__()
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag to convert to HTML")
        if len(self.children) == 0:
            raise ValueError("ParentNode must have children to convert to HTML")
        children_html = ""
        for child in self.children:
            if not isinstance(child, HTMLNode):
                raise TypeError("All children must be instances of HTMLNode")
            else:
                children_html += child.to_html()
        return f'<{self.tag}>{children_html}</{self.tag}>'
