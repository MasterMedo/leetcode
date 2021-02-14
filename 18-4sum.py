class Solution:
    def fourSum(self, arr: list[int], target: int) -> list[list[int]]:
        if len(arr) < 4:
            return []

        arr.sort()
        output = set()
        index = {e: i for i, e in enumerate(arr)}
        for i in range(len(arr) - 3):
            for j in range(i + 1, len(arr) - 2):
                for k in range(j + 1, len(arr) - 1):
                    e = target - arr[i] - arr[j] - arr[k]
                    if e in index and index[e] > k:
                        output.add((arr[i], arr[j], arr[k], e))
        return output
