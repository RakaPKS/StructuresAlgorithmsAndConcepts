# An animal shelter,
# which holds only dogs and cats, operates on a strictly"
# first in, first out" basis. People must adopt either the"oldest"
# (based on arrival time) of all animals at the shelter,
# or they can select whether they would prefer a dog or a cat
# (and will receive the oldest animal of that type).
# They cannot select which specific animal they would like.
# Create the data structures to maintain this system
# and implement operations such as enqueue, dequeueAny, dequeueDog,
# and dequeueCat. You may use the built-in Linked list data structure.

from queue import Queue


class AnimalQueue:
    def __init__(self):
        self.dogQueue = Queue()
        self.catQueue = Queue()
        self.otherQueue = Queue()
        self.counter = 0

    def enqueue(self, name, animal):
        if animal == "dog":
            self.dogQueue.push((name, self.counter))
        if animal == "cat":
            self.catQueue.push((name, self.counter))
        else:
            self.otherQueue.push((name, self.counter))
        self.counter += 1

    def dequeueCat(self):
        result, _ = self.catQueue.pop()
        return result

    def dequeueDog(self):
        result, _ = self.dogQueue.pop()
        return result

    def dequeueOther(self):
        result, _ = self.otherQueue.pop()
        return result

    def dequeueAny(self):
        _, dogAge = self.dogQueue.peek()
        _, catAge = self.catQueue.peek()
        _, otherAge = self.otherQueue.peek()
        oldest = min(dogAge, catAge, otherAge)
        if oldest == dogAge:
            result, _ = self.dogQueue.pop()
        if oldest == catAge:
            result, _ = self.catQueue.pop()
        else:
            result, _ = self.otherQueue.pop()
        return result


animalQueue = AnimalQueue()
animalQueue.enqueue("fluffy", "cat")
animalQueue.enqueue("axel", "dog")
print(animalQueue.dequeueAny())
