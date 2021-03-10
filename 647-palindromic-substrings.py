class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            d = 0
            while i - d >= 0 and i + d < len(s) and s[i - d] == s[i + d]:
                count += 1
                d += 1

            lo, hi = i, i + 1
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                count += 1
                lo -= 1
                hi += 1

        return count
