class Solution:
    def convert(self, s: str, numRows: int) -> str:
        grid = []
        N = len(s)
        for _ in range(numRows):
            grid.append('*' * (N // numRows + 1))
        x, y = 0, 0
        down = True
        right = False
        for i in range(N):
            grid[y][x] = s[i]
            if down:
                y += 1
            else:
                y -= 1
            if right:
                x += 1
            if y == numRows - 1:
                down = False
                right = True
            if y == 0:
                down = True
                right = False
        ans = ""
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != '*':
                    ans += (grid[i][j])
        return ans