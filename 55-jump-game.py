class Solution:
    def canJump(self, arr: list[int]) -> bool:
        closest = 0
        for i in range(len(arr) - 1, 0, -1):
            if arr[i] >= closest:
                closest = 0
            closest += 1

        return arr[0] >= closest
