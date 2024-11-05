from collections import defaultdict, deque

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = defaultdict(deque)
        d['2'] = ['a', 'b', 'c']
        d['3'] = ['d', 'e', 'f']
        d['4'] = ['g', 'h', 'i']
        d['5'] = ['j', 'k', 'l']
        d['6'] = ['m', 'n', 'o']
        d['7'] = ['p', 'q', 'r', 's']
        d['8'] = ['t', 'u', 'v']
        d['9'] = ['w', 'x', 'y', 'z']
        ans = []
        N = len(digits)
        def dfs(s, cnt):
            if cnt == N:
                ans.append(s)
                return
            for c in d[digits[cnt]]:
                dfs(s + c, cnt + 1)
        if N:
            dfs("", 0)
        return ans