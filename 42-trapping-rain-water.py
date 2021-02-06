from collections import deque


class Solution:
    def trap(self, heights: list[int]) -> int:
        left = deque([0])
        for h in heights:
            left.append(max(left[-1], h))
        left.popleft()

        right = deque([0])
        for h in reversed(heights):
            right.appendleft(max(right[0], h))
        right.pop()

        return sum(min(a, b) - h for a, b, h in zip(left, right, heights))
