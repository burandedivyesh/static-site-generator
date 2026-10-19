import sys
sys.path.append(r'/home/thatguy/Personal/Work/thatguy/static-site-generator/src')

import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        html_node = HTMLNode("p", "This is a paragraph.", None, {"href": "https://www.boot.dev",})
        html_node2 = HTMLNode("p", "This is a paragraph.", None, {"href": "https://www.boot.dev",})
        self.assertEqual(html_node, html_node2)

    def test_uneq(self):
        html_node = HTMLNode("p", "This is a paragraph.", None, {"href": "https://www.boot.dev",})
        html_node2 = HTMLNode("t", "This is a not paragraph.", None, {"href": "https://www.boot.dev",})
        self.assertNotEqual(html_node, html_node2)

    def test_props_to_html(self):
        html_node = HTMLNode("p", "This is a paragraph.", None, {"href": "https://www.boot.dev",})
        output = " href=\"https://www.boot.dev\""
        self.assertEqual(html_node.props_to_html(), output)
        



if __name__ == "__main__":
    unittest.main()
