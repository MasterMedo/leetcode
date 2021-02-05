class Solution:
    def intervalIntersection(self, a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
        result = []
        i = j = 0
        while i < len(a) and j < len(b):
            loa, hia = a[i]
            lob, hib = b[j]
            if lob <= hia <= hib:
                result.append([max(loa, lob), min(hia, hib)])
                i += 1
            elif loa <= hib <= hia:
                result.append([max(loa, lob), min(hia, hib)])
                j += 1
            else:
                if hia < hib:
                    i += 1
                else:
                    j += 1
        return result
