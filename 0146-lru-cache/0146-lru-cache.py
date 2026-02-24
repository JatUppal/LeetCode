class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def get(self, key : int):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        else:
            return -1

    def remove(self, node):
        nxt, prv = node.next, node.prev
        nxt.prev = prv
        prv.next = nxt

    def insert(self, node):
        temp = self.right.prev
        temp.next = node
        node.next = self.right
        node.prev = temp
        self.right.prev = node

    def put(self, key : int, value : int):
        node = Node(key, value)
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key] = node
            self.insert(node)
        else:
            if self.size == len(self.cache):
                del self.cache[self.left.next.key]
                self.remove(self.left.next)
            self.insert(node)
            self.cache[key] = node
