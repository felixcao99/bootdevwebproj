import unittest
from markdowntoblocks import *

class TestLeafNode(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_blocktypes(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items

1. This is an ordered list
2. with items

```
This is a code block.
```
"""
        blocks = markdown_to_blocks(md)
        for i in range(len(blocks)):
            block_type = block_to_block_type(blocks[i])
            if i == 0:
                self.assertEqual(block_type, BlockType.PARAGRAPH)
            elif i == 1:
                self.assertEqual(block_type, BlockType.PARAGRAPH)
            elif i == 2:
                self.assertEqual(block_type, BlockType.ULIST)
            elif i == 3:
                self.assertEqual(block_type, BlockType.OLIST)
            elif i == 4:
                self.assertEqual(block_type, BlockType.CODE)
        

if __name__ == "__main__":
    unittest.main()