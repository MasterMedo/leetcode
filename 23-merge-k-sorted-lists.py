from heapq import merge


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def iterator(node: ListNode):
            while node is not None:
                yield node.val
                node = node.next

        if not lists:
            return None

        head = node = ListNode()
        for n in merge(*map(iterator, lists)):
            node.next = ListNode(n)
            node = node.next

        return head.next
