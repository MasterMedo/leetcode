
from heapq import heappush, heappop

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        lists = [l1, l2]
        visit = []
        for i, head in enumerate(lists):
            if head is not None:
                heappush(visit, (head.val, i))

        dummy = node = ListNode()
        while visit:
            _, i = heappop(visit)
            node.next = lists[i]
            node = node.next
            lists[i] = lists[i].next
            if lists[i] is not None:
                heappush(visit, (lists[i].val, i))

        node.next = None
        return dummy.next
