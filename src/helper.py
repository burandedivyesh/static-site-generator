from parentnode import ParentNode
from textnode import InlineTextType, TextNode, text_node_to_leaf_node
from block import BlockType, block_to_blocktype
import re

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: InlineTextType) -> list[TextNode]:
    """
    Converts list of old TextNode(s) to list of new TextNode split according to the delimiter.
    """
    new_nodes = [] # new list of nodes to return

    for node in old_nodes:
        if not(node.text_type == InlineTextType.PLAIN):
            new_nodes.extend([node])
            continue

        if delimiter in node.text:
            if not(node.text.count(delimiter) % 2 == 0):
                raise Exception(f"Matching delimiter{delimiter} not found!")
            else:
                node_split = node.text.split(delimiter)

                for i in range(len(node_split)):
                    if node_split[i] == "":
                        continue
                    if not(i % 2 == 0):
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

BlockTag = {
        BlockType.CODE            : "code",
        BlockType.QUOTE           : "blockquote",
        BlockType.UNORDERED_LIST  : "ul",
        BlockType.ORDERED_LIST    : "ol",
        BlockType.PARAGRAPH       : "p",
        }

def text_to_children(text:str) -> list:
    textnodes = text_to_textnodes(text)
    children = []
    for node in textnodes:
        textnode = text_node_to_leaf_node(node)
        children.append(textnode)

    return children

def create_heading_node(block:str):
    heading_type = {
            "# "         : "h1",
            "## "        : "h2",
            "### "       : "h3",
            "#### "      : "h4",
            "##### "     : "h5",
            "###### "    : "h6",
            }
    heading_tag = ""
    for heading in heading_type.keys():
        if block.startswith(heading):
            block = block.replace(heading, "")
            heading_tag = heading_type[heading]
        continue

    children:list = text_to_children(block)
    heading_node = ParentNode(tag=heading_tag, children=children)
    return  heading_node


def create_code_node(block:str):
    code_text = block.replace("```\n", "").replace("```", "")
    text_node = TextNode(code_text, InlineTextType.CODE)
    code_node = text_node_to_leaf_node(text_node)
    node = ParentNode("pre", children = [code_node])
    return node

def create_quote_node(block:str):
    quote_text = block.replace("> ", "").replace(">", "")
    lines = quote_text.splitlines()
    children = []
    for  line in lines:
        if line == "":
            continue
        children.extend(text_to_children(line))
    quote_node = ParentNode(BlockTag[BlockType.QUOTE], children=children)
    return quote_node


def create_unordered_list_node(block:str):
    """
    An example for unordered_block:
    - item 1
    - item 2
    - item 3
    - item 4
    """
    unord_text = block.replace("- ", "<li>").replace("\n", "</li>")
    children = text_to_children(unord_text)
    unord_node = ParentNode(BlockTag[BlockType.UNORDERED_LIST], children=children)
    return unord_node


def create_ordered_list_node(block:str):
    count = 1
    ord_text = ""
    for line in block.splitlines(block):
        ord_text += line.replace(f"{count}. ", "<li>").replace("\n", "</li>")
        count += 1

    children = text_to_children(ord_text)
    ord_node = ParentNode(BlockTag[BlockType.ORDERED_LIST], children=children)
    return ord_node

def create_paragraph(block:str):
    para_text = block.replace("\n", " ")
    children = text_to_children(para_text)
    para_node = ParentNode(BlockTag[BlockType.PARAGRAPH], children=children)
    return para_node


def markdown_to_htmlnode(markdown:str):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_blocktype(block)

        match block_type:
            case BlockType.HEADING:
                children.append(create_heading_node(block))

            case BlockType.CODE:
                children.append(create_code_node(block))

            case BlockType.QUOTE:
                children.append(create_quote_node(block))

            case BlockType.UNORDERED_LIST:
                children.append(create_unordered_list_node(block))

            case BlockType.ORDERED_LIST:
                children.append(create_ordered_list_node(block))

            case BlockType.PARAGRAPH:
                children.append(create_paragraph(block))

            case _:
                raise Exception("Block of unknown type.")

    return ParentNode("div", children=children)


def extract_title(markdown:str) -> str:
    lines = markdown.splitlines()
    title = ""
    for line in lines:
        if line.startswith("# "):
            title = line.replace("# ", "")
            break

    if title == "":
        raise Exception("No title found!")
    return title
