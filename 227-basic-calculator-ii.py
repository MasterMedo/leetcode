from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        operator = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: b // a
        }
        numbers = deque()
        operators = deque()
        number = []
        priority = False
        for c in s+" ":
            if c.isdigit():
                number.append(c)
            elif number:
                numbers.append(int(''.join(number)))
                number = []
                if priority:
                    numbers.append(operator[operators.pop()](numbers.pop(), numbers.pop()))
                    priority = False
            if c in '+-/*':
                operators.append(c)
                if c in '/*':
                    priority = True

        while operators:
            numbers.appendleft(operator[operators.popleft()](numbers.popleft(), numbers.popleft()))

        return numbers[-1] if numbers else 0
