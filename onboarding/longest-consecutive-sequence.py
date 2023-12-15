class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        mx = 0
        
        for num in st:
            if num - 1 not in st:
                curr = num
                curr_len = 1
                
                while curr + 1 in st:
                    curr += 1
                    curr_len += 1
                
                mx = max(mx, curr_len)
        
        return mx