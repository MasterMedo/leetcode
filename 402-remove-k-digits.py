class Solution:
    def removeKdigits(self, n: str, k: int) -> str:
        stack = []
        for digit in n:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1

            if digit != '0' or stack:
                stack.append(digit)

        return ''.join(stack[:-k or None]) or '0'
