class Solution:
    def diagonalSum(self,matrix):
        n = len(matrix)
        sum_ = 0
        
        for i in range(n):
            sum_ += matrix[i][i]
            sum_ += matrix[i][n - 1 - i]
        
        if n % 2 == 1:
            sum_ -= matrix[n // 2][n // 2]
        
        return sum_   