from Stack import Stack


class MyQueue:
    def __init__(self):
        self.pushStack = Stack()
        self.popStack = Stack()

    def add(self, item):
        if self.popStack.isEmpty():
            self.popStack.push(item)
        else:
            length = len(self.popStack)
            while(not self.popStack.isEmpty()):
                self.pushStack.push(self.popStack.pop())
            self.popStack.push(item)
            for i in range(length):
                self.popStack.push(self.pushStack.pop())
            self.pushStack.push(item)

    def remove(self):
        if self.popStack.isEmpty():
            print("stack is empty")
        else:
            length = len(self.pushStack)
            while(not self.pushStack.isEmpty()):
                self.popStack.push(self.pushStack.pop())
            for i in range(length):
                self.pushStack.push(self.popStack.pop())
            return self.popStack.pop()

    def peek(self):
        return self.popStack.peek()

    def prettyPrint(self):
        self.popStack.prettyPrint()


myQueue = MyQueue()
for i in range(20):
    myQueue.add(i)
myQueue.prettyPrint()
for i in range(10):
    myQueue.remove()
myQueue.prettyPrint()
