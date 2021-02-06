class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            start1, end1 = intervals[i]
            start2, end2 = merged[-1]
            if start2 <= start1 <= end2 or start2 <= end1 <= end2 or start1 <= start2 <= end1:
                merged[-1] = min(start1, start2), max(end1, end2)
            else:
                merged.append([start1, end1])
        return merged
