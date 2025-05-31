import unittest

from src.htmlnode import ParentNode, LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_multiple_children(self):
        grandchild_node = LeafNode("p", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        child_node2 = LeafNode("p", "child2", props={"id": "main", "class": "foo"})
        parent_node = ParentNode("div", [child_node, child_node, child_node2])
        self.assertEqual(
            parent_node.to_html(),
            '<div><span><p>grandchild</p></span><span><p>grandchild</p></span><p id="main" class="foo">child2</p></div>',
        )

    def test_to_html_with_props(self):
        child = LeafNode("p", "ptext")
        parent = ParentNode("section", [child], props={"id": "main", "class": "foo"})
        self.assertEqual(
            parent.to_html(), '<section id="main" class="foo"><p>ptext</p></section>'
        )

    def test_to_html_raises_if_no_tag(self):
        with self.assertRaises(ValueError) as cm:
            ParentNode(None, [LeafNode("span", "x")]).to_html()
        self.assertIn("should have a tag", str(cm.exception))

    def test_to_html_raises_if_no_children(self):
        with self.assertRaises(ValueError) as cm:
            ParentNode("div", None).to_html()
        self.assertIn("should have children", str(cm.exception))

    def test_empty_children_list(self):
        parent = ParentNode("div", [], props=None)
        self.assertEqual(parent.to_html(), "<div></div>")

    def test_parentnode_equality(self):
        a = ParentNode("ul", [LeafNode("li", "1"), LeafNode("li", "2")])
        b = ParentNode("ul", [LeafNode("li", "1"), LeafNode("li", "2")])
        self.assertEqual(a, b)

    def test_parentnode_inequality_different_children(self):
        a = ParentNode("ul", [LeafNode("li", "1")])
        b = ParentNode("ul", [LeafNode("li", "2")])
        self.assertNotEqual(a, b)

    def test_props_none_vs_empty(self):
        a = ParentNode("div", [], props=None)
        b = ParentNode("div", [], props={})
        self.assertEqual(a.to_html(), b.to_html())

    def test_eq_other_type(self):
        node = ParentNode("div", [])
        self.assertFalse(node == "not-a-node")
