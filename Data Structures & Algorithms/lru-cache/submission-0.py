class ListNode:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:

    


    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = ListNode(0,0)
        self.tail = ListNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}

    def insert_back(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev


    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache[key].val
            self.remove(self.cache[key])
            self.insert_back(self.cache[key])
            return val
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key])
            self.insert_back(self.cache[key])
        else:
            self.cache[key] = ListNode(key, value)
            self.insert_back(self.cache[key])
            if len(self.cache) > self.capacity:
                curr = self.head.next
                self.remove(self.head.next)
                del self.cache[curr.key]
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)