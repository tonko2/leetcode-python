class Solution:
    def dfs(self, candidates, equation, v):
        for (c, d), val in list(candidates.items()):
            a, b = equation                        
            if b == c:                
                candidates[(a, d)] = v * val
                candidates[(d, a)] = 1 / candidates[(a, d)]
            if b == d:
                candidates[(a, c)] = v * (1 / val)                
                candidates[(c, a)] = 1 / candidates[(a, c)]
    
    def calcEquation(self, equations, values, queries):
        candidates = dict()
        for i in range(len(equations)):
            a, b = equations[i]
            value = values[i]
            candidates[(a, b)] = value
            candidates[(b, a)] = 1 / value            
            
        ans = []
        while True:
            n = len(candidates)
            for (a, b), value in list(candidates.items()):                
                self.dfs(candidates, (a, b), value)
            if n == len(candidates):
                break
        for a, b in queries:
            if (a, b) not in candidates:
                ans.append(-1)
            else:
                ans.append(candidates[(a, b)])
        return ans