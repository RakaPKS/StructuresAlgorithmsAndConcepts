from Stack import Stack


class StackOfPlates:
    def __init__(self, stackSize):
        self.stackSize = stackSize
        self.stackList = []
        self.emptyPlaces = []
        self.stackList.append(Stack())

    def push(self, item):
        if self.emptyPlaces:
            stackIndex = self.emptyPlaces.pop()
            self.stackList[stackIndex].push(item)
        else:
            if len(self.stackList[-1]) > self.stackSize:
                self.stackList.append(Stack())
            self.stackList[-1].push(item)
        return self.stackList

    def pop(self):
        item = self.stackList[-1].pop()
        if len(self.stackList[-1]) == 0 and len(self.stackList) > 1:
            self.stackList.pop()
        return item

    def peek(self):
        return self.stackList[-1][-1]

    def prettyPrint(self):
        for stack in self.stackList:
            stack.prettyPrint()

    def popAt(self, index):
        if index <= len(self.stackList):
            result = self.stackList[index].pop()
            self.emptyPlaces.append(index)
            return result


stackPlates = StackOfPlates(2)
for i in range(1, 20):
    stackPlates.push(i)
stackPlates.prettyPrint()
stackPlates.pop()
print("Should have one less plate")
stackPlates.prettyPrint()
stackPlates.pop()
print("Should have same amount of plates")
stackPlates.prettyPrint()
stackPlates.popAt(2)
stackPlates.push(50000)
print("Should have 50000 on the third plate")
stackPlates.prettyPrint()
