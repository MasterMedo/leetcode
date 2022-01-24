class SparseVector:
    def __init__(self, nums: list[int]):
        self.vals = []
        self.length = len(nums)
        cnt = 0
        val = nums[0]
        for n in nums:
            if n == val:
                cnt += 1
            else:
                self.vals.append([val, cnt])
                val = n
                cnt = 1

        self.vals.append([val, cnt])

    def dotProduct(self, vec: 'SparseVector') -> int:
        arr1 = [x.copy() for x in self.vals]
        arr2 = [x.copy() for x in vec.vals]
        i1 = i2 = 0
        product = 0
        while i1 < len(arr1) and i2 < len(arr2):
            n1, cnt1 = arr1[i1]
            n2, cnt2 = arr2[i2]
            cnt = min(cnt1, cnt2)
            product += cnt * n1 * n2
            arr1[i1][1] -= cnt
            arr2[i2][1] -= cnt
            if not arr1[i1][1]:
                i1 += 1
            if not arr2[i2][1]:
                i2 += 1

        return product
