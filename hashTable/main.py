# Implementation of a hash table not using dictionary
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self):
        self.capacity = 5000
        self.size = 0
        self.buckets = [None] * self.capacity

    # Never use this hash function it only is an example
    def hash(self, key):
        hashsum = 0
        for idx, c in enumerate(key):
            hashsum += (idx + len(key)) ** ord(c)
            hashsum = hashsum % self.capacity
        return hashsum

    def insert(self, key, value):
        self.size += 1
        index = self.hash(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = Node(key, value)
        else:
            while node:
                node = node.next
            node.next = Node(key, value)

    def get(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        while node and node.key != key:
            node = node.next
        if node is None:
            return None
        return node.value

    def remove(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        previous = None
        while node and node.key != key:
            previous = node
            node = node.next
        if node is None:
            return None
        else:
            self.size -= 1
            result = node.value
            if previous is None:
                self.buckets[index] = node.next
            else:
                previous.next = previous.next.next
                return result


if __name__ == '__main__':
    hashTable = HashTable()
    hashTable.insert("123", "hello")
    hashTable.insert("234", "World")
    print(hashTable.get("123"))
    hashTable.remove("234")
