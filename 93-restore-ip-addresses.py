class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        output = set()
        for i in range(3):
            for j in range(i + 1, i + 4):
                for k in range(j + 1, j + 4):
                    l = k + 1
                    if l < len(s):
                        arr = [s[0:i+1], s[i+1:j+1], s[j+1:k+1], s[k+1:]]
                        if all(int(x) <= 255 and (x[0] != '0' or len(x) == 1) for x in arr):
                            output.add('.'.join(arr))
        return output
