class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast:
            slow = slow.next
            fast = fast.next and fast.next.next
            if fast is not None and fast == slow:
                return True

        return False
