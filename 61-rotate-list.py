class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        node = head
        n = 0
        while node is not None:
            n += 1
            node = node.next

        if n == 0:
            return None

        k %= n
        node = head
        for _ in range(n - k - 1):
            node = node.next

        out = node.next
        if out is None:
            return head

        node.next = None
        if out.next is not None:
            node = out.next
            while node.next is not None:
                node = node.next

            node.next = head
        else:
            out.next = head
        return out
