class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lo_start = lo = ListNode()
        hi_start = hi = ListNode()
        while head is not None:
            if head.val < x:
                lo.next = head
                head = head.next
                lo = lo.next
                lo.next = None
            else:
                hi.next = head
                head = head.next
                hi = hi.next
                hi.next = None

        lo.next = hi_start.next
        return lo_start.next
