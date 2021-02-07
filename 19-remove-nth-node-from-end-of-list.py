class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        for _ in range(n):
            fast = fast.next

        dummy = slow = ListNode(next=head)
        while fast is not None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next
