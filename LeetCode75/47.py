from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        X = [1, 0, -1, 0]
        Y = [0, 1, 0, -1]
        H = len(maze)
        W = len(maze[0])
        visited = [[False] * W for _ in range(H)]
        def bfs(x, y):
            q = deque()
            q.append(((x, y), 0))
            while q:
                (x, y), cnt = q.popleft()
                visited[y][x] = True
                if x == 0 or y == 0 or x == W - 1 or y == H - 1:
                    if not (x == entrance[1] and y == entrance[0]):
                        return cnt
                for i in range(4):
                    nx = x + X[i]
                    ny = y + Y[i]                    
                    if nx < 0 or ny < 0 or nx >= W or ny >= H or maze[ny][nx] == '+' or visited[ny][nx]:
                        continue
                    visited[ny][nx] = True
                    q.append(((nx, ny), cnt + 1))
            return -1
        return bfs(entrance[1], entrance[0])