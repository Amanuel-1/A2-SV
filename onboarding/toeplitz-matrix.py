class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        diag = matrix[0][0]
        n = len(matrix)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i>0 and j>0 and matrix[i-1][j-1] != matrix[i][j]:
                    print("this ",matrix[i][j], matrix[i-1][j-1])
                    return False


        return True

    
