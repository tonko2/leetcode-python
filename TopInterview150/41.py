from collections import defaultdict

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        strs = s.split()
        N = len(pattern)
        if N != len(strs):
            return False
        d = defaultdict(str)
        d2 = defaultdict(str)        
        for i in range(N):
            c1 = pattern[i]
            s2 = strs[i]
            if d[c1] == "":
                d[c1] = s2
            else:
                if d[c1] != s2:
                    return False            
            if d2[s2] == "":
                d2[s2] = c1
            else:
                if d2[s2] != c1:
                    return False            
        return True
        