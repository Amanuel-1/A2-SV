class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        contentChildren  = 0
        # // 7 8 9 10
        # // 5 6 7 8

        g = sorted(g)
        s=sorted(s)
        i,j=0,0
        count=0
        while i<len(g) and j<len(s):
            if s[j]<g[i]:
                j+=1
            else:
                count+=1
                i+=1
                j+=1
        

        return count
            


                

        

        return contentChildren 

        
        
        