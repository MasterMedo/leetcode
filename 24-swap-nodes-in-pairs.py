class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        node = head
        while node is not None and node.next is not None:
            node.val, node.next.val = node.next.val, node.val
            node = node.next.next
        return head
