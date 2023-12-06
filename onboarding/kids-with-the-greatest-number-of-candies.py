class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        largest  =  max(candies)
        result  =[False]*len(candies)
        
        for i in range(len(candies)):
            if candies[i]+extraCandies >=largest:
                result[i]=True
        

        return result
        