class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(next=head)
        node = dummy
        while node.next is not None:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next

        return dummy.next
