from collections import deque


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = deque()
        output = []
        i = 0
        for c in s:
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    continue

            output.append(c)
            i += 1

        while stack:
            output[stack.pop()] = ''

        return ''.join(output)
