import sys
sys.path.append(r'/home/thatguy/Personal/Work/thatguy/static-site-generator/src')
import unittest

from helper import extract_markdown_links, extract_markdown_images

class TestExtractLinkImage(unittest.TestCase):
    def test_extract_link(self):
        md = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_links(md)
        self.assertEqual(matches, [("to boot dev", "https://www.boot.dev"), 
                                   ("to youtube", "https://www.youtube.com/@bootdotdev")])



    def test_extract_image(self):
        md = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_images(md)
        self.assertEqual(matches,[("rick roll","https://i.imgur.com/aKaOqIh.gif"), 
                                  ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])
        
if __name__ == "__main__":
    unittest.main()
