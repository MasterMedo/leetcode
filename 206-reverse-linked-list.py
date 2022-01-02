class Solution:
    def reverseList(self, node: ListNode) -> ListNode:
        if node is None:
            return None

        last = None
        while node.next is not None:
            tmp = node.next
            node.next = last
            last = node
            node = tmp

        node.next = last
        return node
