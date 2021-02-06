class Solution:
    def checkInclusion(self, a: str, b: str) -> bool:
        count = [0] * 26
        for c in a:
            count[ord(c) - 97] += 1

        window = [0] * 26
        for i in range(len(b)):
            if i >= len(a):
                window[ord(b[i-len(a)]) - 97] -= 1
            window[ord(b[i]) - 97] += 1
            if count == window:
                return True
        return False
