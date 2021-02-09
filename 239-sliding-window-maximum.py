from collections import deque


class Solution:
    def maxSlidingWindow(self, arr: list[int], k: int) -> list[int]:
        stack = deque()
        maximums = []
        for i in range(len(arr)):
            while stack and stack[-1][1] < arr[i]:
                stack.pop()

            stack.append((i, arr[i]))
            if stack[0][0] + k <= i:
                stack.popleft()

            if i >= k - 1:
                maximums.append(stack[0][1])

        return maximums
