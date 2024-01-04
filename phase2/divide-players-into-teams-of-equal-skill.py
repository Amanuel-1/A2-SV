class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        skill = sorted(skill)
        i,j  = 0,len(skill)-1

        sum_  = 0
        total_  =skill[i]+skill[j]


        while i<j:
            if skill[i]+skill[j]!= total_:
                return -1
            else:
                sum_ += (skill[i]*skill[j])
                i+=1
                j-=1
        
        return sum_




        