from bisect import bisect_left


class Solution:
    def prevPermOpt1(self, arr: list[int]) -> list[int]:
        for i in range(len(arr) - 2, -1, -1):
            if 0 > i or i >= len(arr):
                break

            if arr[i] > arr[i + 1]:
                j = bisect_left(arr[i + 1:], arr[i])
                while arr[i + j] == arr[i + j - 1]:
                    j -= 1

                if i == i + j:
                    j += 1

                arr[i], arr[i + j] = arr[i + j], arr[i]
                break

        return arr
