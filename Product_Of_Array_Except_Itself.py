class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right =1
        ans=[1 for i in range(len(nums))]
        for i in range(len(nums)-1,-1,-1):
            ans[i]*=right
            right*=nums[i]
        left =1
        for i in range(len(nums)):
            ans[i]*=left
            left*=nums[i]
        print(ans)
        return ans

        
