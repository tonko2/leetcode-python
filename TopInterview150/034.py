class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkArea(x, y):
            s = set()
            for i in range(y, y + 3):
                for j in range(x, x + 3):
                    if board[i][j] == '.':
                        continue
                    if board[i][j] in s:
                        return False
                    s.add(board[i][j])
            return True
        def checkColumn(y):
            s = set()
            for i in range(9):
                if board[y][i] == '.':
                        continue
                if board[y][i] in s:
                    return False
                s.add(board[y][i])
            return True
        def checkRow(x):
            s = set()
            for i in range(9):
                if board[i][x] == '.':
                    continue
                if board[i][x] in s:
                    return False
                s.add(board[i][x])
            return True
        for i in range(9):
            if checkRow(i) == False:
                return False
            if checkColumn(i) == False:
                return False
            if checkArea((i % 3) * 3, (i // 3) * 3) == False:
                return False
        return True