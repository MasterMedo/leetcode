class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        node = head
        for _ in range(k - 1):
            node = node.next

        start = node
        end = head
        while node.next is not None:
            end = end.next
            node = node.next

        start.val, end.val = end.val, start.val
        return head
