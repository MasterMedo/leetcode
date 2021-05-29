class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverse(node, prev=None):
            if node is not None:
                tmp = node.next
                node.next = prev
                return reverse(tmp, node)
            return prev

        l1 = reverse(l1)
        l2 = reverse(l2)
        head = node = ListNode()
        while l1 is not None or l2 is not None:
            node.next = ListNode()
            a = l1.val if l1 is not None else 0
            b = l2.val if l2 is not None else 0
            node.next.val, node.val = divmod(a + b + node.val, 10)
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            last = node
            node = node.next

        if node.val == 0:
            last.next = None

        return reverse(head)
