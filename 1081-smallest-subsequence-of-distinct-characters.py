from collections import Counter


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        counter = Counter(s)
        seen = set()
        for c in s:
            if c not in seen:
                while stack and stack[-1] > c and counter[stack[-1]] > 0:
                    seen.remove(stack.pop())

                stack.append(c)
                seen.add(c)

            counter[c] -= 1

        return ''.join(stack)
