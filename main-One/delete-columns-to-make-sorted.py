class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        matrix=[list(s) for s in strs]
        removed = set()

        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]<matrix[i-1][j]:
                    removed.add(j)


        return len(removed)

        
                               


        return 0