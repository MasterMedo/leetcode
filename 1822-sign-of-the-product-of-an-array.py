class Solution:
    def arraySign(self, arr: list[int]) -> int:
        if not arr:
            return 0

        negatives = 0
        for n in arr:
            if n == 0:
                return 0

            if n < 0:
                negatives += 1

        return 1 if negatives % 2 == 0 else -1
