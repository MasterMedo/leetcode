class Solution:
    def busyStudent(self, start: list[int], end: list[int], query: int) -> int:
        return sum(a <= query <= b for a, b in zip(start, end))
