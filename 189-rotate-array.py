class Solution:
    def rotate(self, arr: list[int], k: int) -> None:
        n = len(arr)
        for i in range(n // 2):
            arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]

        k %= n
        for i in range(k // 2):
            arr[i], arr[k - i - 1] = arr[k - i - 1], arr[i]

        for i in range(k, (k + n) // 2):
            arr[i], arr[n + k - i - 1] = arr[n + k - i - 1], arr[i]
