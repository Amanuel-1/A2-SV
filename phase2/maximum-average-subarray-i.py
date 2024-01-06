class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_ = sum(nums[:k])
        mx  = sum_/k


        for i in range(k,len(nums)):
            sum_-=nums[i-k]
            sum_+=nums[i]
            mx  = max(mx,sum_/k)




        return mx


