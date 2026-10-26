from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    """
    LeafNode represents a HTMLNode which doesn't have children.
    """
    def __init__(self, tag, value, properties=None):
        super().__init__(tag=tag, value=value, children=None, properties=None)
        self.tag = tag
        self.value = value
        self.properties = properties

    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.properties})"

    def to_html(self):
        """
        Renders a html string from LeafNode object.
        Example : LeafNode("p", "This is a paragraph of text.").to_html()
                  "<p>This is a paragraph of text.</p>"
        """
        if self.value == None:
            raise ValueError("LeafNode must have a value.")

        if not self.tag or self.tag == None:
            return str(self.value)


        html_string = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return html_string

    def __eq__(self:LeafNode, other:LeafNode):
        return (self.tag == other.tag \
                and self.value == other.value \
                and self.properties == other.properties)
           

        
        
