class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        output = []
        for i in range(len(arr) - 2):
            if arr[i] > 0:
                break
            if i > 0 and arr[i] == arr[i-1]:
                continue

            j = i + 1
            k = len(arr) - 1
            while j < k:
                s = arr[i] + arr[j] + arr[k]
                if s == 0:
                    output.append([arr[i], arr[j], arr[k]])
                    while j < k and arr[k] == arr[k - 1]:
                        k -= 1
                    while j < k and arr[j] == arr[j + 1]:
                        j += 1
                    k -= 1
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    j += 1

        return output
