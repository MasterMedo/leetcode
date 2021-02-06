class Solution:
    def getIntersectionNode(self, a: ListNode, b: ListNode) -> ListNode:
        if a is None or b is None:
            return None

        i, j = a, b
        while i != j:
            if i is None:
                if b is None:
                    return None
                i = b
                b = None
            else:
                i = i.next

            if j is None:
                if a is None:
                    return None
                j = a
                a = None
            else:
                j = j.next

        return i
