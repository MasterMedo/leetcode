class Solution:
    def insert(self, intervals: list[list[int]], new: list[int]) -> list[list[int]]:
        out = []
        lo, hi = new
        added = False
        for lo_, hi_ in intervals:
            if lo_ <= lo <= hi_ or lo_ <= hi <= hi_ or lo <= lo_ <= hi_ <= hi:
                lo = min(lo, lo_)
                hi = max(hi, hi_)
                continue

            if not added and (lo, hi) < (lo_, hi_):
                out.append([lo, hi])
                added = True

            out.append([lo_, hi_])

        if not added:
            out.append([lo, hi])

        return out
