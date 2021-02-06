from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c in '([{':
                stack.append(c)
            elif c == ')':
                if not stack or stack.pop() != '(':
                    return False
            elif c == ']':
                if not stack or stack.pop() != '[':
                    return False
            elif c == '}':
                if not stack or stack.pop() != '{':
                    return False
            else:
                return False

        return not stack
