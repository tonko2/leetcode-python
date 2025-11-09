class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[False] * m for _ in range(n)]                
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        def dfs(x, y):
            visited[y][x] = True
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if nx < 0 or ny < 0 or nx >= m or ny >= n or grid[ny][nx] == "0" or visited[ny][nx]:
                    continue
                dfs(nx, ny)
        ans = 0
        for i in range(n):
            for j in range(m):
                if visited[i][j] == False and grid[i][j] == "1":
                    dfs(j, i)
                    ans += 1
        return ans