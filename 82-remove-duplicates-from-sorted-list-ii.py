iclass Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        tail = dummy
        while tail.next is not None:
            node = tail.next
            if node.next is not None and node.val == node.next.val:
                while tail.next is not None and tail.next.val == node.val:
                    tail.next = tail.next.next
            else:
                tail = tail.next

        return dummy.next
