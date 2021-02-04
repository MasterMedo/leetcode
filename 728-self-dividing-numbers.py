class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        return [i for i in range(left, right + 1)
                if all(int(d) != 0 and i % int(d) == 0 for d in str(i))]
