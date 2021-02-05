class Solution:
    def rotatedDigits(self, N: int) -> int:
        s = 0
        for i in range(1, N+1):
            invertible = True
            different = False
            for c in str(i):
                if c in '2569':
                    different = True
                elif c in '347':
                    invertible = False

            if invertible and different:
                s += 1

        return s
