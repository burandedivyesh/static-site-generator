from enum import Enum
from leafnode import LeafNode

class InlineTextType(Enum):
    PLAIN      = "plain"
    BOLD       = "bold"
    ITALIC     = "italic"
    CODE       = "code"
    IMAGE      = "image"
    LINK       = "link"


class TextNode:
    """
    TextNode class represents various types of inline text that can exists in both Markdown and HTML.
    """
    def __init__(self,
                 text:str, 
                 text_type:str,
                 url:str = None #default
                 ):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self:TextNode, other:TextNode):
        return ((self.text == other.text) and \
            (self.text_type == other.text_type) and \
            (self.url == other.url))
            

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"



# Function text_node_to_leaf_node -> Converts a TextNode instance to LeafNode instance.
def text_node_to_leaf_node(text_node: TextNode) -> LeafNode:
    match text_node.text_type:
        case InlineTextType.PLAIN:
            return LeafNode(tag=None, value=text_node.text)
        case InlineTextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case InlineTextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case InlineTextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case InlineTextType.IMAGE:
            return LeafNode(tag="img", value="", properties={"src":text_node.url, "alt":text_node.text})
        case InlineTextType.LINK:
            return LeafNode(tag="a", value=text_node.text, properties={"href":text_node.url})
        case _:
            raise Exception("TextNode object of unknown type.")





