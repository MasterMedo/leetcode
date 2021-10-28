class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = head
        while tail is not None:
            while tail.next is not None and tail.val == tail.next.val:
                tail.next = tail.next.next

            tail = tail.next

        return head
