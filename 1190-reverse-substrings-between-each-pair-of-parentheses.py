from collections import deque


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = deque([[]])
        for c in s:
            if c == '(':
                stack.append([])
            elif c == ')':
                temp = stack.pop()
                stack[-1].extend(reversed(temp))
            else:
                stack[-1].append(c)

        return ''.join(stack[0])
