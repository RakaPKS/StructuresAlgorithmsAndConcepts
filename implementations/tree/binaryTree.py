class BinaryTree:
    def __init__(self, root):
        self.root = root


class TreeNode:
    def __init__(self, value, leftChild=None, rightChild=None):
        self.value = value
        self.leftChild = leftChild
        self.rightChild = rightChild

    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.leftChild is None:
                    self.leftChild = TreeNode(value)
                else:
                    self.leftChild.insert(value)
            else:
                if self.rightChild is None:
                    self.rightChild = TreeNode(value)
                else:
                    self.rightChild.insert(value)

    def printTree_in_order(self):
        if self.leftChild:
            self.leftChild.printTree_in_order()
        print(self.value)
        if self.rightChild:
            self.rightChild.printTree_in_order()

    def printTree_pre_order(self):
        print(self.value)
        if self.leftChild:
            self.leftChild.printTree_pre_order()
        if self.rightChild:
            self.rightChild.printTree_pre_order()

    def printTree_post_order(self):
        if self.leftChild:
            self.leftChild.printTree_post_order()
        if self.rightChild:
            self.rightChild.printTree_post_order()
        print(self.value)


root = TreeNode(10)
root.insert(5)
root.insert(8)
root.insert(10)
root.insert(11)
root.insert(10)
root.insert(12)
print("in order")
root.printTree_in_order()
print("pre order")
root.printTree_pre_order()
print("post order")
root.printTree_post_order()
