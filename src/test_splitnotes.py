import unittest

from textnode import *
from leafnode import *
from parentnode import *
from splitnotes import *
from texttotextnodes import *


class TestLeafNode(unittest.TestCase):
    def test_split_bold(self):
        markdown_nodes = [
            TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT),
        ]
        self.assertEqual(split_nodes_delimiter(markdown_nodes, "**", TextType.BOLD), 
                         [TextNode("This is text with a ", TextType.TEXT), 
                          TextNode("bolded phrase", TextType.BOLD),
                          TextNode(" in the middle", TextType.TEXT)
                         ])

    def test_split_code(self):
        markdown_nodes = [
            TextNode("This is text with a `code block` word", TextType.TEXT)
        ]
        self.assertEqual(split_nodes_delimiter(markdown_nodes, "`", TextType.CODE), 
                         [TextNode("This is text with a ", TextType.TEXT),
                          TextNode("code block", TextType.CODE),
                          TextNode(" word", TextType.TEXT),
                         ])
        
    def test_split_code_2(self):
        markdown_nodes = [
            TextNode("`code block` word", TextType.TEXT),
            TextNode(" and another `code block`", TextType.TEXT)
        ]
        self.assertEqual(split_nodes_delimiter(markdown_nodes, "`", TextType.CODE), 
                         [TextNode("code block", TextType.CODE),
                          TextNode(" word", TextType.TEXT),
                          TextNode(" and another ", TextType.TEXT),
                          TextNode("code block", TextType.CODE),                       
                         ])
        
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
        
    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )

    def test_texttotextnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_text_nodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ], 
            new_nodes,
        )

    
if __name__ == "__main__":
    unittest.main()