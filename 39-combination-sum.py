from functools import cache


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()

        @cache
        def helper(target, start=0):
            solutions = []
            for i in range(start, len(candidates)):
                n = candidates[i]
                if n > target:
                    break

                if n == target:
                    solutions.append([n])

                for solution in helper(target - n, i):
                    solutions.append([n] + solution)

            return solutions

        return helper(target)
