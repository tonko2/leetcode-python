from collections import defaultdict

class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        prev = 0
        for c in s[::-1]:
            v = d[c]
            if prev <= v:
                res += v
                prev = d[c]
            else:
                res -= v
                prev = 0
        return res
