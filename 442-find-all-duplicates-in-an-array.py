class Solution:
    def findDuplicates(self, arr: list[int]) -> list[int]:
        result = []
        i = 0
        while i < len(arr):
            n = arr[i] - 1
            if n == i:
                pass

            elif arr[n] == n + 1:
                result.append(n + 1)

            else:
                arr[i], arr[n] = arr[n], arr[i]
                if n >= i:
                    continue
            i += 1

        return result
