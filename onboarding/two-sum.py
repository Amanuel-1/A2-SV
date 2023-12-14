class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      result = []
      for i in range(len(nums)):
        for j in range(len(nums)):
          if nums[i]+nums[j]== target and i!=j:
            result.append(i)
            result.append(j)
        if len(result):
          break
      
      return result
