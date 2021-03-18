# Given a node that is not the first nor last, remove it.
# Cannot access any other node

import sys
sys.path.append("../../LinkedList")
from LinkedList import Node
from LinkedList import LinkedList


def deleteMiddleNode(node):
    if node and node.next:
        node.data = node.next.data
        if node.next.next:
            node.next = node.next.next
        else:
            node.next = None

ll = LinkedList()
first = Node("first")
second = Node("second")
third = Node("third")
last = Node("second")
ll.head = first
first.next = second
second.next = third
third.next = last

deleteMiddleNode(third)
ll.prettyPrint()
