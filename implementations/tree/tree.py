class Tree:
    def __init__(self, root):
        self.root = root

    def prettyPrint(self):
        self.root.prettyPrint()


class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children

    def addChild(self, child):
        self.children.append(child)

    def prettyPrint(self):
        print(self.value)
        if self.children:
            for child in self.children:
                child.prettyPrint()
