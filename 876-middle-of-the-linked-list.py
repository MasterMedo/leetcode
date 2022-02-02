class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = fast = slow = ListNode(next=head)
        while fast is not None:
            fast = fast.next
            slow = slow.next
            if fast is None:
                break

            fast = fast.next

        return slow
