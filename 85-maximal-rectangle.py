class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        running_sum = [0] * len(matrix[0])
        area = 0
        for row in matrix:
            for i, value in enumerate(row):
                if value == "0":
                    running_sum[i] = 0
                else:
                    running_sum[i] += 1
            stack = []
            for i, value in enumerate(running_sum + [0]):
                while stack and running_sum[stack[-1]] >= value:
                    height = running_sum[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    area = max(area, height * width)
                stack.append(i)
        return area
