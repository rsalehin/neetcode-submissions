class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0, 0) # LRU
        self.right = Node(0, 0) # MRU
        self.right.prev = self.left
        self.left.next = self.right
        
    def _remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev


    def _insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next = node
        next.prev = node
        node.next, node.prev = next, prev


    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]



        
