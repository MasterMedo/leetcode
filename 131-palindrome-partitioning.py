class Solution:
    def partition(self, s: str) -> List[List[str]]:
        @cache
        def isPalindrome(s: str) -> bool:
            if len(s) == 1:
                return True
            if len(s) == 2:
                return s[0] == s[-1]
            if s[0] != s[-1]:
                return False
            return isPalindrome(s[1:-1])

        @cache
        def waysToPartition(n: int) -> Set[Tuple[int]]:
            if n == 1:
                return {(1,)}

            ways = {(1,)*n}
            for way in waysToPartition(n - 1):
                for i in range(len(way)):
                    new_way = list(way)
                    new_way[i] += 1
                    ways.add(tuple(new_way))
            return ways

        partitions = []
        for way in waysToPartition(len(s)):
            s_way = []
            i = 0
            for size in way:
                substring = s[i:i + size]
                if not isPalindrome(substring):
                    break
                i += size
                s_way.append(substring)
            else:
                partitions.append(s_way)
        return partitions
