from textnode import InlineTextType, TextNode
import re

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    """
    Converts list of old TextNode(s) to list of new TextNode split according to the delimiter.
    """
    new_nodes : list = [] # new list of nodes to return

    for node in old_nodes:
        if not(node.text_type == InlineTextType.PLAIN):
            new_nodes.extend([node])
            continue

        if delimiter in node.text:
            if not(node.text.count(delimiter) % 2 == 0):
                raise Exception(f"Matching delimiter{delimiter} not found!")
            else:
                node_split = node.text.split(delimiter, maxsplit=2)

                for i in range(len(node_split)):
                    if node_split[i] == "":
                        continue
                    if i == 1:
                        new_nodes.extend([TextNode(node_split[i],text_type,None)])
                        continue
                    new_nodes.extend([TextNode(node_split[i],InlineTextType.PLAIN,None)])

           

        else:
            new_nodes.extend([node])
    
    return new_nodes


def extract_markdown_images(markdown:str):
    """
    Extract images and alt text from text.
    """
    image_pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(image_pattern, markdown)


def extract_markdown_links(markdown:str):
    """
    Extract images and alt text from text.
    """   
    link_pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(link_pattern, markdown)



def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        matches = extract_markdown_images(node.text)
        if not matches:
            new_nodes.extend([node])
            continue
        remaining = node.text
        for _ in matches:
            before, remaining = remaining.split(f"![{_[0]}]({_[1]})", 1)
            if before != "":
                new_nodes.append(TextNode(text=before, 
                                          text_type=InlineTextType.PLAIN, 
                                          url=None))

            new_nodes.append(TextNode(text=_[0], 
                                      text_type=InlineTextType.IMAGE, 
                                      url=_[1]))

        if remaining != "":
            new_nodes.append(TextNode(text=remaining, 
                                      text_type=InlineTextType.PLAIN, 
                                      url= None))

    return new_nodes

# ----------------------------------------------------------------------------------------


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        matches = extract_markdown_links(node.text)
        if not matches:
            new_nodes.extend([node])
            continue
        remaining = node.text
        for _ in matches:
            before, remaining = remaining.split(f"[{_[0]}]({_[1]})", 1)
            if before != "":
                new_nodes.append(TextNode(text=before, 
                                          text_type=InlineTextType.PLAIN, 
                                          url=None))
                
            new_nodes.append(TextNode(text=_[0], 
                                      text_type=InlineTextType.LINK, 
                                      url=_[1]))
        if remaining != "":
            new_nodes.append(TextNode(text=remaining, 
                                      text_type=InlineTextType.PLAIN, 
                                      url= None))

    return new_nodes

def text_to_textnodes(text:str) -> list[TextNode]:
    """
    Sequence here is importatn:
    BOLD -> ITALIC -> CODE -> IMAGE -> LINK
    """
    node = TextNode(text, InlineTextType.PLAIN)
    node = split_nodes_delimiter([node], "**", InlineTextType.BOLD)
    node = split_nodes_delimiter(node, "_", InlineTextType.ITALIC)
    node = split_nodes_delimiter(node, "`", InlineTextType.CODE)
    node = split_nodes_image(node)
    node = split_nodes_link(node)
    return node


def markdown_to_blocks(markdown:str):
    markdown = markdown.strip()
    blocks = markdown.split("\n\n")
    for block in blocks:
        if block == "":
            del block
        else:
            block = block.strip()

    return blocks






