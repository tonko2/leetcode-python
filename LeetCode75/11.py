from collections import deque, defaultdict

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        d = defaultdict(deque)
        for i, c in enumerate(t):
            d[c].append(i)        
        now = 0
        for c in s:            
            while len(d[c]) and now > d[c][0]:
                d[c].popleft()
            if len(d[c]) == 0:
                return False
            now = d[c].popleft()            
        return True