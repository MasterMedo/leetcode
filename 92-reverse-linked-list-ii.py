class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = node = ListNode(next=head)
        for _ in range(left - 1):
            node = node.next

        left_node = prev = node
        node = node.next
        for _ in range(right - left + 1):
            next_ = node.next
            node.next = prev
            prev = node
            node = next_

        left_node.next.next = node
        left_node.next = prev
        return dummy.next
