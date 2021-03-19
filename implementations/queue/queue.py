class Queue:
    def __init__(self):
        self.queue = []

    # Removes and returns top most item in Queue
    def pop(self):
        if self.queue:
            popped = self.queue.pop(0)
            return popped
        print("Queue empty; can't pop on an empty Queue")
        return None

    # Adds item to top of Queue
    def push(self, item):
        self.queue.append(item)

    # Returns top value of Queue
    def peek(self):
        if self.queue:
            return self.queue[0]
        print("Queue empty; can't peek on an empty Queue")
        return None

    def isEmpty(self):
        if self.queue:
            return True
        else:
            return False

    def prettyPrint(self):
        print("Queue: " + str(self.queue))


if __name__ == '__main__':
    queue = Queue()
    for i in range(1, 20):
        queue.push(i)
    print(queue.isEmpty())
    print(str(queue.peek()))
    print(str(queue.pop()))
    queue.prettyPrint()
