class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = tmp = ListNode()
        while l1 is not None or l2 is not None:
            if l1 is not None:
                carry += l1.val
            if l2 is not None:
                carry += l2.val
            carry, val = divmod(carry, 10)
            tmp.next = ListNode(val)
            tmp = tmp.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carry:
            tmp.next = ListNode(carry)
        return head.next
