import sys
sys.path.append(r'/home/thatguy/Personal/Work/thatguy/static-site-generator/src')
import unittest

from textnode import TextNode, InlineTextType
from helper import text_to_textnodes

class TestTexttoTextNode(unittest.TestCase):
    def test_text_to_textnode(self):
        md = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        output = [TextNode("This is ", InlineTextType.PLAIN),
                    TextNode("text", InlineTextType.BOLD),
                    TextNode(" with an ", InlineTextType.PLAIN),
                    TextNode("italic", InlineTextType.ITALIC),
                    TextNode(" word and a ", InlineTextType.PLAIN),
                    TextNode("code block", InlineTextType.CODE),
                    TextNode(" and an ", InlineTextType.PLAIN),
                    TextNode("obi wan image", InlineTextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                    TextNode(" and a ", InlineTextType.PLAIN),
                    TextNode("link", InlineTextType.LINK, "https://boot.dev"),]
        self.maxDiff = None
        self.assertEqual(text_to_textnodes(md), output)


    def test_text_to_textnode2(self):
        md = "This is _text_ with an **bold** word and also a `code block` and an ![dick image](https://i.imgur.com/dick.jpeg) and a [xxx link](https://xxx.dev) lets see what it does to this."
        output = [TextNode("This is ", InlineTextType.PLAIN),
                    TextNode("text", InlineTextType.ITALIC),
                    TextNode(" with an ", InlineTextType.PLAIN),
                    TextNode("bold", InlineTextType.BOLD),
                    TextNode(" word and also a ", InlineTextType.PLAIN),
                    TextNode("code block", InlineTextType.CODE),
                    TextNode(" and an ", InlineTextType.PLAIN),
                    TextNode("dick image", InlineTextType.IMAGE, "https://i.imgur.com/dick.jpeg"),
                    TextNode(" and a ", InlineTextType.PLAIN),
                    TextNode("xxx link", InlineTextType.LINK, "https://xxx.dev"),
                    TextNode(" lets see what it does to this.", InlineTextType.PLAIN),
                  ]
        self.maxDiff = None
        self.assertEqual(text_to_textnodes(md), output)



        
if __name__ == "__main__":
    unittest.main()



