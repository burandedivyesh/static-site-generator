from textnode import InlineTextType, TextNode

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []

    text_types: dict = {"**": InlineTextType.BOLD,
                        "_":  InlineTextType.ITALIC,
                        "`":  InlineTextType.CODE,}

    for node in old_nodes:
        if node.text_type != InlineTextType.PLAIN:
            new_nodes.append(node)
        
        if text_types[delimiter] != text_type:
            raise Exception(f"Incorrect InlineTextType provided for delimiter:{delimiter}")

        if node.text.count(delimiter) != 2:
            raise Exception(f"Matching delimiter:{delimiter} not found")

        # node = "this is a **bold** text."
        node_split = node.text.split(delimiter, 2)

        # node_split = ["this is a ", "bold", " text."]
        new_nodes.extend([TextNode(node_split[0], InlineTextType.PLAIN),  # TextNode("this is a ", InlineTextType.PLAIN)
                          TextNode(node_split[1], text_types[delimiter]),  # TextNode("bold", InlineTextType.BOLD)
                          TextNode(node_split[2], InlineTextType.PLAIN)]) # TextNode(" text", InlineTextType.PLAIN)


    return new_nodes
