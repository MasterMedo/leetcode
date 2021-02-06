class MyLinkedList:
    class Node:
        def __init__(self, val=None, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = MyLinkedList.Node()
        self.tail = self.head
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length or index < 0:
            return -1
        if index == self.length - 1:
            return self.tail.val
        i = 0
        node = self.head.next
        while i < index and node is not None:
            i += 1
            node = node.next

        return node.val

    def addAtHead(self, val: int) -> None:
        self.head.next = MyLinkedList.Node(val, self.head.next)
        if self.tail.next is not None:
            self.tail = self.tail.next
        self.length += 1

    def addAtTail(self, val: int) -> None:
        self.tail.next = MyLinkedList.Node(val)
        self.tail = self.tail.next
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length or index < 0:
            return
        if index == self.length:
            self.addAtTail(val)
        else:
            i = 0
            node = self.head
            while i < index and node is not None:
                i += 1
                node = node.next

            node.next = MyLinkedList.Node(val, node.next)
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length or index < 0:
            return

        i = 0
        node = self.head
        while i < index and node is not None:
            i += 1
            node = node.next

        node.next = node.next.next
        if node.next is None:
            self.tail = node

        self.length -= 1
