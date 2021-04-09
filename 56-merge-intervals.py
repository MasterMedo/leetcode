class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        i = 1
        merged = [intervals[0]]
        while i < len(intervals):
            lo, hi = intervals[i]
            if lo <= merged[-1][-1]:
                if hi > merged[-1][-1]:
                    merged[-1][-1] = hi
            else:
                merged.append([lo, hi])
            i += 1

        return merged
