from enum import Enum

class BlockType(Enum):
    PARAGRAPH         = "paragraph"
    HEADING           = "headign"
    CODE              = "code"
    QUOTE             = "quote"
    UNORDERED_LIST    = "unordered_list"
    ORDERED_LIST      = "ordered_list"

def block_to_blocktype(block:str) -> BlockType:
    # HEADING
    heading_types = ("# ", "## ", "### ", "#### ", "##### ", "###### ")
    if block.startswith(heading_types):
        return BlockType.HEADING

    # CODE
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE

    # QUOTE
    quote_flag = True
    for line in block.splitlines():
        if not (line.startswith("> ") or line.startswith(">")):
            # print("Block can't be parsed. (QUOTE)")
            quote_flag = False

    if quote_flag:
        return BlockType.QUOTE

    # UNORDERED
    unordered_flag = True
    for line in block.splitlines():
        if not(line.startswith("- ")):
            # print("Block can't be parsed. (UNORDERED)")
            unordered_flag = False

    if unordered_flag:
        return BlockType.UNORDERED_LIST

    # ORDERED
    count = 1
    ordered_flag = True
    for line in block.splitlines():
        if not(line.startswith(f"{count}. ")):
            # print("Block can't be parsed. (ORDERED)")
            ordered_flag = False
        count+=1

    if ordered_flag:
        return BlockType.ORDERED_LIST

    # PARAGRAPH -> default
    return BlockType.PARAGRAPH

