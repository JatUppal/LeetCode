class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node):
        temp = self.right.prev
        self.right.prev = node
        node.prev = temp
        node.next = self.right
        temp.next = node
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache.keys():
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            self.remove(self.cache[key])
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])
        else:
            self.cache[key] = Node(key, value)
            if self.size < len(self.cache):
                del self.cache[self.left.next.key]
                self.remove(self.left.next)
                self.insert(self.cache[key])
            else:
                self.insert(self.cache[key])





# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)