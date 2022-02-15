class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        dp = left = right = points[0]
        for i in range(1, len(points)):
            left[0] = dp[0]
            for j in range(1, len(left)):
                left[j] = max(dp[j], left[j - 1] - 1)

            right[-1] = dp[-1]
            for j in range(len(right) - 2, -1, -1):
                right[j] = max(dp[j], right[j + 1] - 1)

            for j in range(len(dp)):
                dp[j] = max(dp[j], left[j], right[j]) + points[i][j]

        return max(dp)
