from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        def my_print():
            for row in matrix:
                print(row)
            print()
        
        n = len(matrix)
        # Transpose the matrix                
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            my_print()
        
        # Reverse each row
        for i in range(n):
            matrix[i].reverse()
        
if __name__ == '__main__':
    s = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    s.rotate(matrix)