class Solution:
    def findMedianSortedArrays(self, x, y):
        length = len(x) + len(y)
        arr = [0] * length
        i = j = k = 0
        while i < len(x) or j < len(y):
            if i < len(x) and (j >= len(y) or x[i] < y[j]):
                arr[k] = x[i]
                i += 1
            else:
                arr[k] = y[j]
                j += 1
            k += 1

        return arr[length//2] if length & 1 else (arr[length//2-1] + arr[length//2])/2
