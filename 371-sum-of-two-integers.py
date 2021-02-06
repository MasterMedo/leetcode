class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffff
        while b != 0:
            a, b = (a ^ b) & mask, (a & b) << 1 & mask

        return a if a < 0x7fff else ~(a ^ mask)
