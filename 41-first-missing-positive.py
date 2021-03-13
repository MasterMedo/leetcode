class Solution:
    def firstMissingPositive(self, arr: list[int]) -> int:
        missing = set(range(1, len(arr) + 2))
        for n in arr:
            if n in missing:
                missing.remove(n)

        return missing.pop()
