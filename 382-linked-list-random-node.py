from random import random


class Solution:
    def __init__(self, head: ListNode):
        self.head = head

    def getRandom(self) -> int:
        node = self.head.next
        r = random()
        v = self.head.val
        while node is not None:
            r1 = random()
            if r1 > r:
                r = r1
                v = node.val

            node = node.next
        return v
