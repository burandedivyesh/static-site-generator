from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, properties=None):
        super().__init__(tag=tag, value=None, children=None, properties=properties)
        self.tag = tag
        self.children = children
        self.properties = properties

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.properties})"

    def __eq__(self:ParentNode, other:ParentNode):
        return (self.tag == other.tag \
                and self.children == other.children \
                and self.properties == other.properties)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag.")

        if not self.children:
            raise ValueError("ParentNode must have at least one child.")

        html_string = ""

        for _ in self.children:
            html_string += _.to_html()

        # LeafNode.to_html()
        # eg : html_string = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return f"<{self.tag}{self.props_to_html()}>{html_string}</{self.tag}>"
