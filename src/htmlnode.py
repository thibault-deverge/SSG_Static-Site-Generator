class HTMLNode:
    def __init__(
        self,
        tag: str = None,
        value: str = None,
        children: list["HTMLNode"] = None,
        props: dict = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def __eq__(self, other: "HTMLNode") -> bool:
        if not isinstance(other, HTMLNode):
            return False
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props_to_html() == other.props_to_html()
        )

    def to_html(self):
        raise NotImplementedError("to_html() should be implemented in child class.")

    def props_to_html(self):
        if self.props == None:
            return ""

        props_str = ""
        for key, value in self.props.items():
            props_str += f'{key}="{value}" '
        return props_str[:-1]


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list["HTMLNode"], props: dict = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        prop_str = ""

        if self.tag == None:
            raise ValueError("ParentNode should have a tag")
        if self.children == None:
            raise ValueError("ParentNode should have children node")
        if self.props:
            prop_str = " " + self.props_to_html()

        children_html = "".join([child.to_html() for child in self.children])

        return f"<{self.tag}{prop_str}>{children_html}</{self.tag}>"


class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str = None, props: dict = None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        prop_str = ""

        if self.value == None:
            raise ValueError("all leaf nodes must have a value")
        if self.tag == None:
            return self.value
        if self.props:
            prop_str = " " + self.props_to_html()

        if self.value == "":
            return f"<{self.tag}{prop_str} />"
        else:
            return f"<{self.tag}{prop_str}>{self.value}</{self.tag}>"
