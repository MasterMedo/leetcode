class Solution:
    def numberOfBeams(self, arr: List[str]) -> int:
        ans = 0
        n = 0
        for s in arr:
            devices = s.count("1")
            if devices:
                ans += n * devices
                n = devices
        return ans
