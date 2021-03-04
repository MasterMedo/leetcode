class Solution:
    def numDecodings(self, s: str) -> int:
        if s == '':
            return 0

        last_digit = ''
        ways = 1
        prev = 0
        for digit in s:
            tmp = ways
            ways = (digit != '0') * ways + (9 < int(last_digit + digit) < 27) * prev
            prev = tmp
            last_digit = digit

        return ways
