class LFUCache:
    class Node:
        def __init__(self, key, val=0, prev=None, next_=None, count=0):
            self.key = key
            self.val = val
            self.prev = prev
            self.next = next_
            self.count = count

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        node.count += 1
        if node.next is None or node.next.count > node.count:
            return node.val

        prev = node.prev
        next_ = node.next
        if prev is not None:
            prev.next = next_
        if next_ is not None:
            next_.prev = prev

        if node == self.head:
            self.head = next_

        while next_ is not None and next_.count <= node.count:
            next_ = next_.next

        if next_ is None:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            node.next = None

        else:
            prev = next_.prev
            prev.next = node
            node.prev = prev
            next_.prev = node
            node.next = next_

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.get(key)
            self.cache[key].val = value

        elif self.capacity <= 0:
            return
        else:
            if self.capacity == 1:
                self.head = None
                self.tail = None
                self.cache = {}

            elif len(self.cache) >= self.capacity:
                del self.cache[self.head.key]
                self.head = self.head.next
                self.head.prev = None

            node = LFUCache.Node(key, value)
            self.cache[key] = node
            if self.tail is None:
                self.head = node
                self.tail = node
                node.count = 1
            else:
                self.head.prev = node
                node.next = self.head
                self.head = node
                self.get(key)
