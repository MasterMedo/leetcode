from math import inf


class Solution:
    def threeSumClosest(self, arr: list[int], target: int) -> int:
        arr.sort()
        number = diff = inf
        for i in range(len(arr) - 2):
            lo, hi = i + 1, len(arr) - 1
            while lo < hi:
                s = arr[i] + arr[lo] + arr[hi]
                d = abs(target - s)
                if d < diff:
                    diff = d
                    number = s
                    if diff == 0:
                        return target

                if s < target:
                    lo += 1
                else:
                    hi -= 1
        return number
