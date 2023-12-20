class Solution:

    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ones = sum(nums)
        zeros =0
        answer  =[0]*len(nums)
        mp= defaultdict(list)
        mx =-float('inf')

        for i in range(len(nums)):
            mp[zeros+ones].append(i)
            mx =max(mx,ones+zeros)
            if nums[i]==0:
                zeros+=1
            else:
                ones-=1
        mx=max(mx,zeros+ones)
        mp[zeros+ones].append(len(nums))


        return mp[mx]


        