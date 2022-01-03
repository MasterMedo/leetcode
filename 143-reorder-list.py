class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = node = tail = ListNode(next=head)
        cnt = 0
        while tail.next is not None:
            tail = tail.next
            cnt += 1

        for _ in range(cnt - cnt // 2):
            node = node.next

        prev = node
        for _ in range(cnt // 2):
            node.next, node, prev = prev, node.next, node

        node.next = prev
        node = dummy
        while cnt > 0:
            node.next = head
            node = node.next
            head = head.next
            cnt -= 1
            if cnt <= 0:
                break

            node.next = tail
            node = node.next
            tail = tail.next
            cnt -= 1

        node.next = None
        return dummy.next
