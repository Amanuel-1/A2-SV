class Solution:
    def average(self, salary: List[int]) -> float:
        sum_ = 0
        mn,mx =10**6 +7,1000


        for s in salary:
            sum_ +=s
            mn =min(mn,s)
            mx = max(mx,s)

        return (sum_-mx-mn)/(len(salary)-2)
        
        