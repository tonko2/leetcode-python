from collections import deque, defaultdict
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)        
        q = deque()
        q.append((0, 1))
        visited = [False] * (n * n)        
        jump = defaultdict(int)
        for i in range(n):
            for j in range(n):
                c = j if i % 2 == 0 else n - j - 1
                if board[n - i - 1][c] != -1:
                    jump[i * n + j + 1] = board[n - i - 1][c]        
        while q:
            roll, current = q.popleft()            
            if visited[current - 1]:
                continue
            visited[current - 1] = True
            if current == n * n:
                return roll
            for i in range(6):
                if current + i + 1 > n * n:
                    continue
                if jump[current + i + 1]:
                    q.append((roll + 1, jump[current + i + 1]))
                else:
                    q.append((roll + 1, current + i + 1))
        return -1

s = Solution()    
board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
print(s.snakesAndLadders(board))

