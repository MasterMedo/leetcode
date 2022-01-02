class Solution:
    def myAtoi(self, s: str) -> int:
        limit = pow(2, 31)
        low, high = -limit, limit-1

        n = 0
        chars = []
        sign = None
        for c in s:
            if c == ' ' and sign is None and not chars:
                continue

            elif c in '-+' and sign is None and not chars:
                sign = 1 if c == '+' else -1

            elif c in '1234567890':
                chars.append(c)

            else:
                break

        for i, c in enumerate(reversed(chars)):
            n += int(c) * pow(10, i)

        if sign is not None:
            n *= sign

        return min(high, max(low, n))
