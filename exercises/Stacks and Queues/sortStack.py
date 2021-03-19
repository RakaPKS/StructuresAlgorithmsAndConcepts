from Stack import Stack


def sortStack(stack):
    tmp = 0
    result = Stack()
    while(not stack.isEmpty()):
        tmp = stack.pop()
        while not result.isEmpty() and result.peek() > tmp:
            stack.push(result.pop())
        result.push(tmp)
    while(not result.isEmpty()):
        stack.push(result.pop())
    return stack


stack = Stack()
stack.push(5)
stack.push(3)
stack.push(2)
stack.push(6)
stack.push(7)
stack.prettyPrint()
sortStack(stack).prettyPrint()
