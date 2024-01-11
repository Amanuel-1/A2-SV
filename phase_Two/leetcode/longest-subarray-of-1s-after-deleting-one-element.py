class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        j = 0  
        k = 1  
        mx = 0
        
        while j < len(nums):
            if nums[j] == 0:
                if k > 0:
                    k -= 1
                    j += 1
                elif k <= 0:
                    k = k + 1 if nums[i] == 0 else k
                    i += 1
            else:
                j += 1
            mx = max(mx, j - i)
        
        return mx - 1