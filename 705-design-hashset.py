from math import inf


class MyHashSet:
    class Node:
        def __init__(self, key=inf, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def add(self, node) -> None:
            if node.key == self.key:
                return
            elif node.key < self.key:
                if self.left is None:
                    self.left = node
                else:
                    self.left.add(node)
            else:
                if self.right is None:
                    self.right = node
                else:
                    self.right.add(node)

        def remove(self, key: int) -> None:
            if key == self.key:
                assert False
            elif key < self.key:
                if self.left is not None:
                    if self.left.key == key:
                        if self.left.left is None:
                            self.left = self.left.right
                        elif self.left.right is None:
                            self.left = self.left.left
                        else:
                            left, right = self.left.left, self.left.right
                            self.left = right
                            right.add(left)
                    else:
                        self.left.remove(key)
            else:
                if self.right is not None:
                    if self.right.key == key:
                        if self.right.left is None:
                            self.right = self.right.right
                        elif self.right.right is None:
                            self.right = self.right.left
                        else:
                            left, right = self.right.left, self.right.right
                            self.right = right
                            right.add(left)
                    else:
                        self.right.remove(key)

        def contains(self, key: int) -> bool:
            if key == self.key:
                return True
            elif key < self.key:
                if self.left is None:
                    return False
                return self.left.contains(key)
            else:
                if self.right is None:
                    return False
                return self.right.contains(key)

    def __init__(self):
        self.size = 2441
        self.arr = [MyHashSet.Node() for _ in range(self.size)]

    def hash(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        self.arr[self.hash(key)].add(MyHashSet.Node(key))

    def remove(self, key: int) -> None:
        self.arr[self.hash(key)].remove(key)

    def contains(self, key: int) -> bool:
        return self.arr[self.hash(key)].contains(key)
