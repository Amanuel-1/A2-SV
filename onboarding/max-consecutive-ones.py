class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i,j=0,0

        mx = 0

        while j<len(nums):
            if nums[i]==0:
                i+=1
                j+=1
            elif nums[j]==1:
                mx = max(mx,j-i+1)
                j+=1
            else:
                j+=1
                i=j

        return mx