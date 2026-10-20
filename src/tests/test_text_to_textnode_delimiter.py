import sys
sys.path.append(r'/home/thatguy/Personal/Work/thatguy/static-site-generator/src')

import unittest

from textnode import TextNode, InlineTextType
from helper import split_nodes_delimiter

class TestTexttoTextNodeDelimiter(unittest.TestCase):
    def test_eq(self):
        md = "this is a **bold** text"
        node = TextNode(md, InlineTextType.PLAIN)
        old_nodes = [node]
        new_nodes = split_nodes_delimiter(old_nodes, "**", InlineTextType.BOLD)
        self.assertSequenceEqual(new_nodes, 
                                 [TextNode("this is a ", InlineTextType.PLAIN),
                                  TextNode("bold", InlineTextType.BOLD),
                                  TextNode(" text", InlineTextType.PLAIN)]) 

    def test_eq1(self):
        md = "this is a _italic_ text"
        node = TextNode(md, InlineTextType.PLAIN)
        old_nodes = [node]
        new_nodes = split_nodes_delimiter(old_nodes, "_", InlineTextType.ITALIC)
        self.assertSequenceEqual(new_nodes, 
                                 [TextNode("this is a ", InlineTextType.PLAIN),
                                  TextNode("italic", InlineTextType.ITALIC),
                                  TextNode(" text", InlineTextType.PLAIN)]) 


    def test_uneq(self):
        md = "this is a _italic_ text"
        node = TextNode(md, InlineTextType.PLAIN)
        old_nodes = [node]
        new_nodes = split_nodes_delimiter(old_nodes, "_", InlineTextType.ITALIC)
        self.assertNotEqual(new_nodes, 
                                 [TextNode("this is a ", InlineTextType.PLAIN),
                                  TextNode("italic", InlineTextType.BOLD),
                                  TextNode(" text", InlineTextType.PLAIN)]) 

            

if __name__ == "__main__":
    unittest.main()
 

