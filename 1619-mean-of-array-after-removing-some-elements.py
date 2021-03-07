class Solution:
    def trimMean(self, arr: list[int]) -> float:
        arr.sort()
        five_percent = int(len(arr) * 0.05)
        return sum(arr[five_percent:-five_percent]) / len(arr) / 0.9
