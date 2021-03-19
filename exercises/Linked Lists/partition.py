from LinkedList import LinkedList, Node


def naiveFillSmallLinkedList(val, nodeList, node):
    if node is None:
        node = Node(val)
        nodeList.head = node
    else:
        temp = Node(val)
        node.next = temp
        node = node.next
    return node, nodeList


def naivePartition(ll, x):
    if ll.head is None:
        return None
    small = LinkedList()
    large = LinkedList()
    smallNode = None
    largeNode = None

    node = ll.head
    while node:
        if node.data < x:
            smallNode, small = naiveFillSmallLinkedList(
                node.data, small, smallNode)
        else:
            largeNode, large = naiveFillSmallLinkedList(
                node.data, large, largeNode)
        node = node.next
    if small.head:
        if large.head:
            smallNode.next = large.head
        return small
    else:
        return large.head


def optimizedPartition(ll, x):
    if ll.head is None:
        return None
    head = ll.head
    tail = ll.head
    inspecting = ll.head

    while inspecting:
        next = inspecting.next
        if inspecting.data < x:
            inspecting.next = head
            head = inspecting
        else:
            tail.next = inspecting
            tail = inspecting
        inspecting = next
    tail.next = None

    result = LinkedList()
    result.head = head
    return result


ll = LinkedList()
first = Node(5)
second = Node(3)
third = Node(7)
last = Node(1)
ll.head = first
first.next = second
second.next = third
third.next = last

naivePartition(ll, 5).prettyPrint()
optimizedPartition(ll, 5).prettyPrint()
