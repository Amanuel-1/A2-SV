class Solution:
    def missingNumber(self, nums: List[int]) -> int:
      nums = sorted(nums)
      i=0
      while i<len(nums):
        if nums[i]!=i:
          return i
        i+=1
      return i
      
