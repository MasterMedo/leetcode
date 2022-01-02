class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a = eval(a.replace('i', 'j'))
        b = eval(b.replace('i', 'j'))
        ab = a * b
        return f'{ab.real:.0f}+{ab.imag:.0f}i'
