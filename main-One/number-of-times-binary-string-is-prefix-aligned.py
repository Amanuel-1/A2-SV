class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        mx = 0
        total =0
        count =0

        for i in range(len(flips)):
            total+=flips[i]
            mx = max(mx,flips[i])
            if total ==(mx*(mx+1)/2):
                count+=1



        return count


        