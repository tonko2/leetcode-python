import copy

class Solution:
    
    def changeCell(self, b: List[List[int]], y, x, n, m):        
        dx = [1, 0, -1, 0, 1, 1, -1, -1]
        dy = [0, 1, 0, -1, 1, -1, 1, -1]
        one = 0        
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if b[ny][nx] == 1:
                one += 1
        if b[y][x] == 0 and one == 3:
            return 1
        if b[y][x] == 1 and (one == 2 or one == 3):
            return 1          
        return 0
    
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        b = copy.deepcopy(board)
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                board[i][j] = self.changeCell(b, i, j, n, m)
        