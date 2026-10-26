import unittest
from helper import extract_title

class TestExtractTitle(unittest.TestCase):
    def testextractitle(self):
        md = "# this is heading!"
        title = extract_title(md)
        self.assertEqual(title, "this is heading!")

    def testextractitle2(self):
        md = """
# this is heading!
## this is heading 2

this is a paragraph.

- item 1
- item 2
- item 3
    """
        title = extract_title(md)
        self.assertEqual(title, "this is heading!")
    
