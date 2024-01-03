class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        next_nonzero = 0

        for n  in nums:
            if n!=0:
                nums[next_nonzero] =n
                next_nonzero+=1
        print(next_nonzero)
        for i in range(next_nonzero,len(nums)):
            nums[i]=0
        
        