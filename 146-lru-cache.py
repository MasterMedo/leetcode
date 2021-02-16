class LRUCache:
    class Node:
        def __init__(self, key=0, val=0, left=None, right=None):
            self.key = key
            self.val = val
            self.left = left
            self.right = right

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = LRUCache.Node()
        self.tail = self.head
        self.keys = {}

    def _prefix(self, node: Node) -> None:
        right = self.head.right
        node.right = right
        node.left = self.head
        self.head.right = node
        if right is not None:
            right.left = node

        if self.tail.right is not None:
            self.tail = self.tail.right

    def _move(self, key: int) -> None:
        node = self.keys[key]
        if node.left is not self.head:
            if node == self.tail:
                self.tail = node.left
            node.left.right = node.right
            if node.right is not None:
                node.right.left = node.left
            self._prefix(node)

    def get(self, key: int) -> int:
        if key in self.keys:
            self._move(key)
            return self.keys[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            self.keys[key].val = value
            self._move(key)
            return

        if len(self.keys) >= self.capacity:
            del self.keys[self.tail.key]
            self.tail = self.tail.left
            self.tail.right = None

        node = LRUCache.Node(key, value)
        self._prefix(node)
        self.keys[key] = node
