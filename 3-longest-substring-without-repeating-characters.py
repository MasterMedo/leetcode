class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_ = 0
        last = -1
        for i, c in enumerate(s):
            if c in seen:
                last = max(last, seen[c])

            max_ = max(max_, i - last)
            seen[c] = i
        return max_
