import sys
sys.path.append(r'/home/thatguy/Personal/Work/thatguy/static-site-generator/src')
import unittest

from helper import split_nodes_image, split_nodes_link
from textnode import TextNode, InlineTextType

class TestExtractLinkImage(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            InlineTextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", InlineTextType.PLAIN),
                TextNode("image", InlineTextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", InlineTextType.PLAIN),
                TextNode("second image", InlineTextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )   


    def test_split_links(self):
        node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    InlineTextType.PLAIN,)

        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", InlineTextType.PLAIN),
                TextNode("to boot dev", InlineTextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", InlineTextType.PLAIN),
                TextNode("to youtube", InlineTextType.LINK, "https://www.youtube.com/@bootdotdev"),
            ],
            new_nodes,
        )   


if __name__ == "__main__":
    unittest.main()
