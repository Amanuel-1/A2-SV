class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        mp=defaultdict(int)
        current =0

        for n in nums:
            if n not in mp:
                nums[current]=n
                current+=1

            mp[n]+=1
        
                    
        return current