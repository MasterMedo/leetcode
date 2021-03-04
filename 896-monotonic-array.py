class Solution:
    def isMonotonic(self, arr: list[int]) -> bool:
        decided = False
        inc = False
        e = arr[0]
        for i in range(1, len(arr)):
            if not decided:
                if arr[i] != e:
                    decided = True
                    inc = arr[i] > e
            elif inc:
                if arr[i] < e:
                    return False
            else:
                if arr[i] > e:
                    return False
            e = arr[i]

        return True
