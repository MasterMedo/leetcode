class Solution:
    def sortColors(self, arr: list[int]) -> None:
        zeros = ones = 0
        for n in arr:
            if n == 0:
                zeros += 1
            elif n == 1:
                ones += 1

        for i in range(len(arr)):
            if zeros:
                arr[i] = 0
                zeros -= 1
            elif ones:
                arr[i] = 1
                ones -= 1
            else:
                arr[i] = 2
