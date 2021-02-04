class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        lo, hi = 0, len(s)
        arr = []
        for c in s:
            if c == 'I':
                arr.append(lo)
                lo += 1
            else:
                arr.append(hi)
                hi -= 1

        arr.append(hi)
        return arr
