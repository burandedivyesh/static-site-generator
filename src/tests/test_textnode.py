import sys
sys.path.append(r'/home/thatguy/Personal/Work/thatguy/static-site-generator/src')
import unittest
from textnode import TextNode, InlineTextType, text_node_to_leaf_node
from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        text_node = TextNode("This is a text node", InlineTextType.BOLD)
        text_node2 = TextNode("This is a text node", InlineTextType.BOLD)
        self.assertEqual(text_node, text_node2)

    def test_uneq(self):
        text_node = TextNode("This is a text node", InlineTextType.BOLD)
        text_node2 = TextNode("This is a text node", InlineTextType.ITALIC)
        self.assertNotEqual(text_node, text_node2)

    def test_url_none(self):
        text_node = TextNode("This is a text node without a url", InlineTextType.BOLD)
        self.assertEqual(text_node.url, None)

    def test_textnode_to_leafnode(self):
        text_node = TextNode("This is a link", InlineTextType.LINK, url="https://www.boot.dev")
        leaf_node = LeafNode(tag="a", value="This is a link", properties={"href":"https://www.boot.dev"})
        self.assertEqual(text_node_to_leaf_node(text_node), leaf_node)

    def test_textnode_to_leafnode2(self):
        text_node = TextNode("This is a image", InlineTextType.IMAGE, url="https://www.boot.dev/boots.png")
        leaf_node = LeafNode(tag="img", value="", properties={"src":"https://www.boot.dev/boots.png", "alt":"This is a image"})
        self.assertEqual(text_node_to_leaf_node(text_node), leaf_node)

    def test_textnode_to_leafnode2(self):
        text_node = TextNode("This is a plain text", InlineTextType.PLAIN)
        leaf_node = LeafNode(tag=None, value="This is a plain text")
        self.assertEqual(text_node_to_leaf_node(text_node), leaf_node)




if __name__ == "__main__":
    unittest.main()
