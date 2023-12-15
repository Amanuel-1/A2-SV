class Solution:
  def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
    mp = defaultdict(int)
    for i, n in enumerate(nums):
      mp[n] = i
    
    for num1,num2 in operations:

      nums[mp[num1]] = num2
      mp[num2] = mp[num1]
    
    return nums