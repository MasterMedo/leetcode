from bisect import bisect_left, insort


class Solution:
    def medianSlidingWindow(self, arr: list[int], k: int) -> list[float]:
        arr.append(0)
        window = sorted(arr[:k])
        medians = []
        for i in range(k, len(arr)):
            medians.append((window[k // 2] + window[-(k // 2) - 1]) / 2)
            old = bisect_left(window, arr[i-k])
            del window[old]
            insort(window, arr[i])

        return medians
