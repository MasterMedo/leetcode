class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        arr = []
        i = 0
        for c in s:
            if c == ')':
                i -= 1

            if i != 0:
                arr.append(c)

            if c == '(':
                i += 1

        return ''.join(arr)
