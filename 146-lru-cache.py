class LRUCache:
    class Node:
        def __init__(self, key, val=0, prev=None, next_=None):
            self.key = key
            self.val = val
            self.prev = prev
            self.next = next_

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        if node == self.tail:
            return node.val

        prev = node.prev
        next_ = node.next
        if prev is not None:
            prev.next = next_

        if next_ is not None:
            next_.prev = prev

        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        if node == self.head and self.head.next is not None:
            self.head = self.head.next
            self.head.prev = None

        node.next = None
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.get(key)
            self.tail.val = value

        else:
            node = LRUCache.Node(key, value, self.tail)
            if self.tail is None:
                self.head = node
                self.tail = node
            else:
                self.tail.next = node
                self.tail = node

            if len(self.cache) >= self.capacity:
                del self.cache[self.head.key]
                self.head = self.head.next
                self.head.prev = None

            self.cache[key] = node
