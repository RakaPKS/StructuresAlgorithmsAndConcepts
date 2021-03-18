# Python implementation of a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prettyPrint(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def addFirst(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def addLast(self, data):
        if not self.tail:
            temp = self.head
            while temp:
                self.tail = temp
                temp = temp.next
        newNode = Node(data)
        self.tail.next = newNode
        self.tail = newNode

    def removeItem(self, data):
        if self.head.data == data:
            self.head = self.head.next
        temp = self.head
        while temp:
            if temp is not self.tail and temp.next.data == data:
                if temp.next == self.tail:
                    temp.next = None
                else:
                    temp.next = temp.next.next
            temp = temp.next


if __name__ == '__main__':
    lList = LinkedList()
    first = Node("first")
    second = Node("second")
    lList.head = first
    lList.head.next = second
    lList.addLast("last")
    lList.addFirst("negativeFirst")
    lList.removeItem("second")
    lList.prettyPrint()
