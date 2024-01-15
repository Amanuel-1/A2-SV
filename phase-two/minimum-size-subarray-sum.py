class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        minRange = float('inf')
        i, j = 0, 0
        currSum = 0

        while j < n:
            currSum += nums[j]

            while currSum >= target:
                minRange = min(minRange, j - i + 1)
                currSum -= nums[i]
                i += 1

            j += 1

        return minRange if minRange != float('inf') else 0