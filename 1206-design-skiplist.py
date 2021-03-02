from random import random


class Skiplist:
    class Node:
        def __init__(self, val=-1, prev=None, next=None, up=None, down=None):
            self.val = val
            self.prev = prev
            self.next = next
            self.up = up
            self.down = down

    def __init__(self):
        self.head = self.tail = Skiplist.Node()
        self.height = 1

    def search(self, target: int) -> bool:
        node = self.head
        while node is not None:
            if node.val == target:
                return True
            if node.next is not None and node.next.val <= target:
                node = node.next
            else:
                node = node.down

        return False

    def add(self, target: int) -> None:
        node = self.head
        rightmost = []
        while node is not None:
            if node.next is not None and node.next.val <= target:
                node = node.next

            elif node.down is not None:
                rightmost.append(node)
                node = node.down
            else:
                height = 0
                tmp = Skiplist.Node(target, prev=node, next=node.next)
                if node.next is not None:
                    node.next.prev = tmp

                node.next = tmp
                while random() >= 0.5:
                    height += 1
                    if height >= self.height:
                        self.head = Skiplist.Node(down=self.head)
                        self.height += 1

                    node = rightmost[-height] if height <= len(rightmost) else self.head

                    tmp.up = Skiplist.Node(target, prev=node, next=node.next, down=tmp)
                    tmp = tmp.up
                    if node.next is not None:
                        node.next.prev = tmp

                    node.next = tmp
                return True

        return False

    def erase(self, target: int) -> bool:
        node = self.head
        while node is not None:
            if node.val == target:
                while node is not None:
                    node.up = None
                    if node.prev is not None:
                        node.prev.next = node.next
                    if node.next is not None:
                        node.next.prev = node.prev
                    tmp = node.down
                    node.down = None
                    node = tmp

                return True

            if node.next is not None and node.next.val <= target:
                node = node.next
            else:
                node = node.down

        return False
