from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mp  =  defaultdict(int)

        for n in nums:
            mp[n]+=1
        
        n = len(nums)
        ans = []

        for m in mp:
            if mp[m] > n//3:
                ans.append(m)
        

        
        return ans


        