# Given a linked list l:
# 1) Remove all duplicates
# 2) Remove all duplicates without buffer


import sys
sys.path.append("../../LinkedList")
from LinkedList import LinkedList
from LinkedList import Node


# with buffer

def removeDuplicates(ll):
    prev = None
    items = []
    if ll.head:
        temp = ll.head
        while temp:
            if temp.data in items:
                if temp.next:
                    prev.next = temp.next
                else:
                    prev.next = None
            else:
                items.append(temp.data)
            prev = temp
            temp = temp.next
    return ll

# without buffer


def removeDuplicatesWithoutBuffer(ll):
    if ll.head:
        temp = ll.head
        while temp:
            prev = temp
            nxt = temp.next
            while nxt:
                if nxt.data == temp.next.data:
                    if nxt.next:
                        prev.next = nxt.next
                else:
                    prev.next = None
                prev = nxt
                nxt = nxt.next
            temp = temp.next
    return ll


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

removeDuplicates(ll).prettyPrint()
removeDuplicatesWithoutBuffer(ll).prettyPrint()
