from collections import Counter
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
      mp = {}
      result = []

      for i in nums:
          if i not in mp:
              mp[i] = 0
          mp[i] += 1

      cuml = 0

      for i in sorted(mp.keys()):
          mp[i], cuml = cuml, cuml + mp[i]
          
      for i in nums:
          result.append(mp[i])

      return result
            
        
                