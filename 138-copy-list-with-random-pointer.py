from collections import defaultdict


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        copy = defaultdict(lambda: Node(0))
        copy[None] = None

        node = head
        while node:
            copy[node].val = node.val
            copy[node].next = copy[node.next]
            copy[node].random = copy[node.random]
            node = node.next

        return copy[head]
