class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        #  1 2 2 4 7 8
        piles = sorted(piles)

        j= len(piles)-2
        i = 0
        sum_ =0

        while i<j:
            sum_+=piles[j]
            j-=2
            i+=1
        

        return sum_




        