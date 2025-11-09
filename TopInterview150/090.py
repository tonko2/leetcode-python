from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        
        n = len(board)
        m = len(board[0])
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        
        def dfs(x, y):
            if x < 0 or y < 0 or x >= m or y >= n or board[y][x] != "O":
                return
            board[y][x] = "#"
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                dfs(nx, ny)
        
        for i in range(n):
            if board[i][0] == "O":
                dfs(0, i)
            if board[i][m - 1] == "O":
                dfs(m - 1, i)
        
        for j in range(m):
            if board[0][j] == "O":
                dfs(j, 0)
            if board[n - 1][j] == "O":
                dfs(j, n - 1)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"


if __name__ == "__main__":
    # Test case 1: Example from LeetCode
    board1 = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    expected1 = [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"],
    ]

    solution = Solution()
    solution.solve(board1)
    print("Test 1:")
    print("Result:", board1)
    print("Expected:", expected1)
    print("Pass:", board1 == expected1)
    print()

    # Test case 2: All O's on border (should remain)
    board2 = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]
    expected2 = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]

    solution.solve(board2)
    print("Test 2:")
    print("Result:", board2)
    print("Expected:", expected2)
    print("Pass:", board2 == expected2)
    print()

    # Test case 3: Single cell
    board3 = [["X"]]
    expected3 = [["X"]]

    solution.solve(board3)
    print("Test 3:")
    print("Result:", board3)
    print("Expected:", expected3)
    print("Pass:", board3 == expected3)

    board4 = [
        ["X", "O", "X", "X"],
        ["O", "X", "O", "X"],
        ["X", "O", "X", "O"],
        ["O", "X", "O", "X"],
    ]
    expected4 = [
        ["X", "O", "X", "X"],
        ["O", "X", "X", "X"],
        ["X", "X", "X", "O"],
        ["O", "X", "O", "X"],
    ]
    
    solution.solve(board4)
    print("Test 4:")
    print("Result:", board4)
    print("Expected:", expected4)
    print("Pass:", board4 == expected4)