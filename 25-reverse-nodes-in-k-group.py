class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = prev_head = prev = ListNode(next=head)
        node = head
        counter = 0
        while node is not None:
            tail = node.next
            node.next = prev
            prev = node
            counter += 1
            if counter >= k:
                head.next = tail
                prev_head.next = node
                prev_head = head
                head = head.next
                counter = 0

            node = tail

        while node != head:
            tmp = prev.next
            prev.next = node
            node = prev
            prev = tmp

        return dummy.next
