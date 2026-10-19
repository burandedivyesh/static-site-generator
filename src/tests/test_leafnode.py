import sys
sys.path.append(r'/home/thatguy/Personal/Work/thatguy/static-site-generator/src')

import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_node_with_props(self):
        # LeafNode without properties
        output = "<p>This is a paragraph of text.</p>"
        leaf_node = LeafNode("p", "This is a paragraph of text.") 
        self.assertEqual(leaf_node.to_html(), output)

    def test_leaf_node_without_props(self):
        # LeafNode with properties
        leaf_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        output = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(leaf_node.to_html(), output)

    def test_eq(self):
        leaf_node  = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        leaf_node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(leaf_node, leaf_node2)
        



if __name__ == "__main__":
    unittest.main()
