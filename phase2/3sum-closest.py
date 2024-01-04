class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
      nums = sorted(nums)
      closest = float('inf')
      
      for i in range(len(nums)-2):
        j,k =i,len(nums)-1

        while j<k:
          if j==i:
            j+=1
          if k==i:
            k-=1
          sum_ =nums[i]+nums[j]+nums[k]
          if sum_ ==target:
            return sum_
          if abs(sum_ -target) <= abs(closest -target):
            closest =sum_
          if sum_ <=target :
            j+=1
          else:
            k-=1
      return closest
          


