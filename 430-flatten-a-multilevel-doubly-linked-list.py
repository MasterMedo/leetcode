from collections import deque


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        nodes = deque()
        dummy = node = Node(next=head)
        while node.next is not None or nodes:
            if node.next is None:
                tmp = nodes.pop()
                node.next = tmp
                tmp.prev = node

            node = node.next
            if node.child is not None:
                if node.next is not None:
                    nodes.append(node.next)

                node.next = node.child
                node.child.prev = node

            node.child = None

        return dummy.next
