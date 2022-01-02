class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        ans.add(tuple())
        for i in nums:
            new = set()
            for t in ans:
                new.add(tuple(sorted(t + (i,))))
            ans = ans.union(new)
        return ans
