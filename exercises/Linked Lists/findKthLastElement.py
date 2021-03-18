# Find k-th last element in a single linked list

import sys
sys.path.append("../../LinkedList")
from LinkedList import Node
from LinkedList import LinkedList


def findKthElement(node, k, n=0):
    if node:
        item, m = findKthElement(node.next, k, n+1)
        #print("k" + str(k))
        #print("n" + str(n))
        #print("m" + str(m))
        if m-n == k:
            return (node, m)
        else:
            return(item, m)
    else:
        return (None, n)


# generate linked list
ll = LinkedList()
first = Node("first")
second = Node("second")
third = Node("third")
last = Node("second")
ll.head = first
first.next = second
second.next = third
third.next = last

node, _ = findKthElement(ll.head, 2)
print(node.data)
