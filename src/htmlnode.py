class HTMLNode:
    """
    "HTMLNode" class will represent a "node" in an HTML document tree (like a <p> tag and its contents, or an <a> tag and its contents). 
    It can be block level or inline, and is designed to only output HTML.
    """
    def __init__(self,
                 tag:str=None, # HTML tag name
                 value:str=None, # Value of tag
                 children:list=None, # List representing any nested children
                 properties:dict=None # HTML attributes of the tag
                 ):
        self.tag = tag
        self.value = value
        self.children = children
        self.properties = properties

    def to_html(self):
        """
        Child classes will override this method to implement their own.
        """
        raise NotImplementedError

    def props_to_html(self):
        attr = ""
        if not self.properties:
            return attr # Returns empty str if None

        for k,v in self.properties.items():
            attr += f" {k}=\"{v}\""

        return attr

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.properties})"

    def __eq__(self:HTMLNode, another:HTMLNode):
        return (self.tag == another.tag \
                and self.value == another.value \
                and self.children == another.children \
                and self.properties == another.properties)









