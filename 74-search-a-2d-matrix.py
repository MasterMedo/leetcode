class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo = 0
        hi = len(matrix) * len(matrix[0]) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            r, c = divmod(mid, len(matrix[0]))
            if matrix[r][c] < target:
                lo = mid + 1
            elif matrix[r][c] > target:
                hi = mid
            else:
                lo = mid
                break

        r, c = divmod(lo, len(matrix[0]))
        return matrix[r][c] == target
