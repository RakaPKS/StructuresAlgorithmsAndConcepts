# Stack Min: How would you design a stack which,
# in addition to push and pop, has a function min which
# returns the minimum element?
# Push, pop and min should all operate in 0(1) time.

from Stack import Stack


def superPush(primaryStack, minStack, value):
    if minStack.isEmpty():
        minStack.push(value)
    else:
        if minStack.peek() >= value:
            minStack.push(value)
    primaryStack.push(value)
    return primaryStack, minStack


def superPop(primaryStack, minStack):
    if minStack.isEmpty() or primaryStack.isEmpty():
        print("err stacks are empty")
    else:
        value = primaryStack.pop()
        if minStack.peek() == value:
            minStack.pop()
    return primaryStack, minStack


if __name__ == '__main__':
    primaryStack = Stack()
    minStack = Stack()

    for i in range(1, 20):
        if i == 15:
            primaryStack, minStack = superPush(primaryStack, minStack, 25)
        primaryStack, minStack = superPush(primaryStack, minStack, 20-i)
    primaryStack.prettyPrint()
    minStack.prettyPrint()

    for i in range(1, 6):
        primaryStack, minStack = superPop(primaryStack, minStack)
        primaryStack.prettyPrint()
        minStack.prettyPrint()
