from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        pos = set()
        res = []
        x, y = 0, 0
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        direction = 0
        N = len(matrix)
        M = len(matrix[0])
        while len(res) != N * M:
            res.append(matrix[y][x])
            pos.add((x, y))
            nx = x + dx[direction]
            ny = y + dy[direction]
            if (nx, ny) in pos or nx < 0 or nx >= M or ny < 0 or ny >= N:
                direction = (direction + 1) % 4
                nx = x + dx[direction]
                ny = y + dy[direction]
            x = nx
            y = ny
        return res
    
    
if __name__ == '__main__':
    test = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(test.spiralOrder(matrix))