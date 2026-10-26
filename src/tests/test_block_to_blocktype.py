import sys
sys.path.append(r'/home/thatguy/Personal/Work/thatguy/static-site-generator/src')
import unittest

from block import block_to_blocktype, BlockType
from helper import markdown_to_blocks

class TestBlocktoBlockType(unittest.TestCase):
    def test_heading_block(self):
        blocks = markdown_to_blocks("### heading 4")
        block = blocks[0]
        self.assertEqual(block_to_blocktype(block), BlockType.HEADING)

    def test_code_block(self):
        code = """
```
print("this is a python code")
```
"""
        blocks = markdown_to_blocks(code)
        block = blocks[0]
        self.assertEqual(block_to_blocktype(block), BlockType.CODE)

    def test_quote_block(self):
        quote = """
> quote 1
>quote 2
"""
        blocks = markdown_to_blocks(quote)
        block = blocks[0]
        self.assertEqual(block_to_blocktype(block), BlockType.QUOTE)

    def test_unordered_list(self):
        unordered = """
- item 1
- item 2
- item 3
"""
        
        blocks = markdown_to_blocks(unordered)
        block = blocks[0]
        self.assertEqual(block_to_blocktype(block), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        ordered = """
1. item 1
2. item 2
3. item 3
"""
        
        blocks = markdown_to_blocks(ordered)
        block = blocks[0]
        self.assertEqual(block_to_blocktype(block), BlockType.ORDERED_LIST)

    def test_unordered_list1(self):
        unordered = """
- item 1
item 2
- item 3
"""
        
        blocks = markdown_to_blocks(unordered)
        block = blocks[0]
        self.assertNotEqual(block_to_blocktype(block), BlockType.UNORDERED_LIST)

    def test_ordered_list1(self):
        ordered = """
1. item 1
item 2
3. item 3
"""
        
        blocks = markdown_to_blocks(ordered)
        block = blocks[0]
        self.assertNotEqual(block_to_blocktype(block), BlockType.ORDERED_LIST)


if __name__ == "__main__":
    unittest.main()
