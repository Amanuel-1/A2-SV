class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dxn  = [(0,1),(1,0),(0,-1),(-1,0)]
        visited = set()
        mx = 0
        Area =0
        def search(i,j):
            nonlocal mx
            nonlocal Area
            if i<0 or j<0 or i>=len(grid) or  j>=len(grid[0]) or (i,j) in visited or grid[i][j]==0 :
               
                return
            else:
                Area+=1
                mx = max(mx,Area)
                visited.add((i,j))

                for x,y in dxn:
                    search(i+x,j+y)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and (i,j) not in visited:
                    search(i,j)
                    Area=0

        return mx


                

