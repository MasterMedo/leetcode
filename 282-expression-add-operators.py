class Solution:
    def addOperators(self, digits: str, target: int) -> list[str]:
        def dfs(digits, expression, value, prev):
            nonlocal output, target
            if not digits:
                if value == target:
                    output.append(expression)
                return

            for i in range(len(digits)):
                left = digits[:i+1]
                n = int(left)
                if i == 0 or digits[0] != '0':
                    dfs(digits[i+1:], expression + '+' + left, value + n, n)
                    dfs(digits[i+1:], expression + '-' + left, value - n, -n)
                    dfs(digits[i+1:], expression + '*' + left, value - prev + prev * n, prev * n)

        output = []
        for i in range(len(digits)):
            if i == 0 or digits[0] != '0':
                rest = digits[:i+1]
                n = int(rest)
                dfs(digits[i+1:], rest, n, n)
        return output
