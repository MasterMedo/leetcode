from functools import cache


class Solution:
    def numRollsToTarget(self, dice: int, faces: int, target: int) -> int:
        @cache
        def dfs(dice_left: int, n: int) -> int:
            if dice_left == 0 and n == target:
                return 1

            if n >= target or dice_left <= 0:
                return 0

            return sum(dfs(dice_left - 1, n + roll) for roll in range(1, faces + 1)) % mod

        mod = 10**9 + 7
        return dfs(dice, 0)
