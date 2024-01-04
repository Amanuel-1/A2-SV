class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        i,j  = 0, len(nums)-1
        total=0


        while i<j:
            sum_  =  nums[i]+nums[j]
            if sum_ >k:
                j-=1
            elif sum_<k:
                i+=1
            else:
                total+=1
                i+=1
                j-=1

        return total