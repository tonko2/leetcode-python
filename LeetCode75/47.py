from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        ans = 0
        q = deque()
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 2:
                    q.append(((j, i), 0))
        X = [1, 0, -1, 0]
        Y = [0, 1, 0, -1]
        while q:
            (x, y), cnt = q.popleft()
            ans = max(ans, cnt)
            for i in range(4):
                nx = x + X[i]
                ny = y + Y[i]
                if nx < 0 or ny < 0 or nx >= N or ny >= M or grid[ny][nx] != 1:
                    continue
                grid[ny][nx] = 2
                q.append(((nx, ny), cnt + 1))
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    return -1
        return ans
        