class Solution:
    def countSubstrings(self, s: str) -> int:
        seen = set()
        count = 0
        for window in range(len(s)):
            for lo in range(len(s) - window):
                hi = lo + window
                if s[lo] == s[hi] and (lo + 1 > hi - 1 or (lo + 1, hi - 1) in seen):
                    count += 1
                    seen.add((lo, hi))
        return count
