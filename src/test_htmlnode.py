import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_eq_1(self):
        node = HTMLNode()
        node.props = {"class": "test", "id": "node1"}
        self.assertEqual(' class="test" id="node1"', node.props_to_html())

    def test_eq_2(self):
        node = HTMLNode()
        node.props = {"href": "https://www.google.com", "target": "_blank"}
        self.assertEqual(' href="https://www.google.com" target="_blank"', node.props_to_html())

    def test_neq(self):
        node = HTMLNode()
        node.props = {"class": "test", "id": "node1"}
        self.assertNotEqual(' class="test" id="node2"', node.props_to_html())

if __name__ == "__main__":
    unittest.main()