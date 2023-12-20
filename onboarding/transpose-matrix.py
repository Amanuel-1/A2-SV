class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result =[]
        for i in range(len(matrix[0])):
            result.append([0]*len(matrix))

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                result[j][i]=matrix[i][j]
        

        return result