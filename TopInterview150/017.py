class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        curr = 0
        N = len(s)
        ans = 0
        while curr < N:
            val1 = d[s[curr]]
            if curr + 1 < N:            
                val2 = d[s[curr + 1]]
                if val1 < val2:
                    ans += val2 - val1
                    curr += 1
                else:
                    ans += val1
            else:
                ans += val1
            curr += 1
        return ans
                    