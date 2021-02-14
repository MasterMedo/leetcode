class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        nominator = abs(dividend)
        denominator = abs(divisor)
        quotient = 0
        for i in range(31, -1, -1):
            if nominator >> i >= denominator:
                quotient += 1 << i
                nominator -= denominator << i

        return quotient * pow(-1, (dividend < 0) != (divisor < 0))
