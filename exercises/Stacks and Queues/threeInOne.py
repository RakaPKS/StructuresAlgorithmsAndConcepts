# Describe how you could use a single array to implement three stacks.
# Implementation?
# Divide array by three. Index is i % 3
# if array is full, copy array and double size

import numpy as np


class ThreeInOneArray:
    def __init__(self):
        self.stackArray = np.zeros(3)
        self.headOne = -3
        self.headTwo = -2
        self.headThree = -1

    def determineHead(self, queueNr):
        if queueNr == "first":
            return self.headOne
        if queueNr == "second":
            return self.headTwo
        if queueNr == "third":
            return self.headThree

    def incrementHead(self, queueNr):
        if queueNr == "first":
            self.headOne += 3
        if queueNr == "second":
            self.headTwo += 3
        if queueNr == "third":
            self.headThree += 3

    def increaseArray(self):
        self.stackArray.resize(len(self.stackArray)*2)

    def pop(self, queueNr):
        head = self.determineHead(queueNr)
        result = self.stackArray[head]
        self.stackArray[head] = 0
        return result

    def push(self, queueNr, item):
        head = self.determineHead(queueNr)
        if len(self.stackArray) <= head+3:
            self.increaseArray()
        self.stackArray[head+3] = item
        self.incrementHead(queueNr)

    def peek(self, queueNr):
        head = self.determineHead(queueNr)
        return self.stackArray[head]

    def isEmpty(self):
        return (self.stackArray == np.zeros(len(self.stackArray))).all()

    def prettyPrint(self):
        print("Stack: " + str(self.stackArray))


stack = ThreeInOneArray()
print(stack.isEmpty())
stack.push("first", 2)
stack.push("first", 2)
stack.push("first", 2)
stack.push("first", 2)
stack.push("second", 3)
stack.push("second", 3)
stack.push("second", 3)
stack.push("second", 3)
stack.push("third", 6)
stack.push("third", 6)
stack.push("third", 6)
stack.push("third", 6)
stack.prettyPrint()
print(stack.isEmpty())
print(stack.pop("first"))
print(stack.pop("second"))
print(stack.pop("third"))
print(stack.pop("third"))
print(stack.pop("third"))
stack.prettyPrint()
