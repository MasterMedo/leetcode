from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        length = 0
        chars = deque()
        for c in s:
            if c in seen:
                while True:
                    last = chars.popleft()
                    seen.remove(last)
                    if last == c:
                        break
            chars.append(c)
            seen.add(c)
            length = max(length, len(chars))

        return length
