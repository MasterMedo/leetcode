from itertools import zip_longest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(i) for i in version1.split('.')]
        v2 = [int(i) for i in version2.split('.')]
        for a, b in zip_longest(v1, v2, fillvalue=0):
            if a > b:
                return 1
            if b > a:
                return -1
        return 0
