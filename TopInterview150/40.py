from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = defaultdict(str)
        d2 = defaultdict(str)
        N = len(s)
        for i in range(N):
            c1 = s[i]
            c2 = t[i]          
            if d[c1] == "":
                d[c1] = c2
            else:
                if d[c1] != c2:
                    return False            
            if d2[c2] == "":
                d2[c2] = c1
            else:
                if d2[c2] != c1:
                    return False            
        return True
            