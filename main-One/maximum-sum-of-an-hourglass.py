class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:

        mx=0
        sm = 0
        for i in range(len(grid)-2):

            for j in range(len(grid[0])-2):
                sm=0
                sm += sum(grid[i][j:j+3])
                sm+=grid[i+1][j+1]
                sm+= sum(grid[i+2][j:j+3])

                mx = max(mx,sm)
 

                
        return mx