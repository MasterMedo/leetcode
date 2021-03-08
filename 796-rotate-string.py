class Solution:
    def rotateString(self, a: str, b: str) -> bool:
        if len(a) != len(b):
            return False

        if len(a) == 0:
            return len(b) == 0

        for _ in range(len(a)):
            if a == b:
                return True

            a = a[1:] + a[0]

        return False
