class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums  = sorted(nums,reverse = True)

        for i in range(len(nums)-2):
            if nums[i]<(nums[i+1]+nums[i+2]):
                return nums[i]+nums[i+1]+nums[i+2]
    
            # 9 4 4 2 1
            # 10 2 1 1


        return 0



        return 0