class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        i = 0
        while z != 0:
            z &= z - 1
            i += 1

        return i
