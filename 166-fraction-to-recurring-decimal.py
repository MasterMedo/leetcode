class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if denominator == 0:
            return '0'

        result = []
        if denominator < 0 and numerator > 0 or denominator > 0 and numerator < 0:
            result.append('-')
            numerator, denominator = abs(numerator), abs(denominator)

        d, m = divmod(numerator, denominator)

        result.append(str(d))

        if m == 0:
            return ''.join(result)

        result.append('.')
        seen = {}
        while m != 0:
            if m in seen:
                result.append(')')
                return ''.join(e if i != seen[m] else '('+e for i, e in enumerate(result))

            seen[m] = len(result)
            d, m = divmod(m*10, denominator)
            result.append(str(d))
        return ''.join(result)
