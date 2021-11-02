from math import factorial as f


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k -= 1
        arr = list(range(1, n + 1))
        indices = []
        step = f(n)
        while k != 0:
            step //= n
            i, k = divmod(k, step)
            indices.append(i)
            n -= 1

        result = []
        for i in indices:
            result.append(arr[i])
            del arr[i]

        return "".join(map(str, result + arr))
