from collections import deque


class Solution:
    def nextLargerNodes(self, head: ListNode) -> list[int]:
        node = head
        vals = []
        while node is not None:
            vals.append(node.val)
            node = node.next

        ans = [0]
        stack = deque()
        for i in range(len(vals) - 1, 0, -1):
            if vals[i] > vals[i - 1]:
                ans.append(vals[i])
                stack.append(vals[i])
            else:
                while stack and stack[-1] <= vals[i - 1]:
                    stack.pop()
                if stack:
                    ans.append(stack[-1])
                else:
                    ans.append(0)

        return ans[::-1]
