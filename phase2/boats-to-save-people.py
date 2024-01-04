class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        boats   = 0
        people  = sorted(people)
        i,j  = 0,len(people)-1
        singleFlag  = False
        while i<j:
            if people[i]+people[j]<=limit:
                boats+=1
                i+=1
                j-=1
            else:
                boats+= 1
                j-=1
        if i==j:
            boats+=1
            
        return boats

        # 1 2 2 3
        