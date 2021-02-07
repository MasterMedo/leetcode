class Solution:
    def multiply(self, a: str, b: str) -> str:
        output = [0] * (len(a) + len(b))
        for i, x in enumerate(reversed(a)):
            for j, y in enumerate(reversed(b)):
                output[i + j] += int(x) * int(y)

        carry = 0
        for i in range(len(output)):
            carry, output[i] = divmod(output[i] + carry, 10)

        output = ''.join(str(digit) for digit in reversed(output)).lstrip('0')
        return output if output else '0'
