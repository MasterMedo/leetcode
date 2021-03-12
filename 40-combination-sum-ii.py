class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        dp = {(0, tuple())}
        for n in candidates:
            dp |= {(s + n, arr + (n, )) for s, arr in dp if s + n <= target}

        return [arr for s, arr in dp if s == target]
