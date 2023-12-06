class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        result  = []

        for i in range(0,len(nums)-1,2):
            result += [nums[i+1]]* (nums[i])
        

        return result
        