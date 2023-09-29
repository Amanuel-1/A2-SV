class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        dxn =  [(0,1),(0,-1),(1,0),(-1,0)]
        source = image[sr][sc]

        def explore(i,j):
            if i<0 or i>=len(image) or j<0 or j>=len(image[0]):
                return
            
            elif image[i][j]==color:
                return
            elif image[i][j]!=source:
                return
            else:
                if image[i][j]==source:
                    image[i][j]=color
                    for (x,y) in dxn:
                        explore(i+x,j+y)
        explore(sr,sc)
        return image

                

        
