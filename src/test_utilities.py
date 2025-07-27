import unittest
from utilities import *


class TestHTMLNode(unittest.TestCase):
    def test_extract_title(self):
        markdown = """# Sample Title
This is a paragraph.
Another paragraph."""
        self.assertEqual('Sample Title', extract_title(markdown))

if __name__ == "__main__":
    unittest.main()