from itertools import product, permutations
from operator import mul, truediv, add, sub
from contextlib import suppress
from math import isclose


class Solution:
    def judgePoint24(self, numbers: list[int]) -> bool:
        f = {'*': mul, '/': truediv, '+': add, '-': sub}
        for a, b, c, d in permutations(numbers):
            for op1, op2, op3 in product(f, repeat=3):
                with suppress(ZeroDivisionError):
                    if isclose(f[op3](f[op2](f[op1](a, b), c), d), 24):
                        return True

                with suppress(ZeroDivisionError):
                    if isclose(f[op3](f[op1](a, b), f[op2](c, d)), 24):
                        return True

                with suppress(ZeroDivisionError):
                    if isclose(f[op3](f[op2](c, f[op1](a, b)), d), 24):
                        return True

                with suppress(ZeroDivisionError):
                    if isclose(f[op3](d, f[op2](c, f[op1](a, b))), 24):
                        return True

                with suppress(ZeroDivisionError):
                    if isclose(f[op1](a, f[op3](f[op2](b, c), d)), 24):
                        return True

        return False
