class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        def getRow(g, r):
            res = []
            for i in range(len(g)):
                res.append(g[i][r])
            return res
        N = len(grid)
        ans = 0
        for i in range(N):
            for j in range(N):
               if grid[i] == getRow(grid, j):
                   ans += 1
        return ans