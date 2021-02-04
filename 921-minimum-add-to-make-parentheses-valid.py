class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = steps = 0
        for c in s:
            if c == '(':
                count += 1

            elif c == ')':
                count -= 1
                if count < 0:
                    steps += 1
                    count = 0

        return steps + count
