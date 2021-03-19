class Stack:
    def __init__(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)

    # Removes and returns top most item in stack

    def pop(self):
        if self.stack:
            popped = self.stack[-1]
            del(self.stack[-1])
            return popped
        print("Stack empty; can't pop on an empty stack")
        return None

    # Adds item to top of stack
    def push(self, item):
        self.stack.append(item)

    # Returns top value of stack
    def peek(self):
        if self.stack:
            return self.stack[-1]
        print("Stack empty; can't peek on an empty stack")
        return None

    def isEmpty(self):
        if self.stack:
            return False
        else:
            return True

    def prettyPrint(self):
        print("Stack: " + str(self.stack))


if __name__ == '__main__':
    stack = Stack()
    print(stack.isEmpty())
    for i in range(1, 20):
        stack.push(i)
    print(stack.isEmpty())
    print(str(stack.peek()))
    print(str(stack.pop()))
    stack.prettyPrint()
