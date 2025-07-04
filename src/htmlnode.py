class HTMLNode:
    def __init__(self):
        self.tag = None
        self.value = None
        self.children = None
        self.props = None
    
    def to_html(self):
        raise NotImplementedError("Subclasses should implement this method")
    
    def props_to_html(self):
        if not self.props:
            return ""
        html = ""
        for s in self.props:
            html += f' {s}="{self.props[s]}"'
        return html
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"