class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        pref  =[0]
        mp  = defaultdict(int)
        for i in range(len(nums)):
            pref.append(pref[i]+nums[i])
        
        i=0
        mx =0

        for j in range(len(nums)):
            mp[nums[j]]+=1
            while len(mp)< j-i+1:
                mp[nums[i]]-=1
                if mp[nums[i]]==0:
                    del mp[nums[i]]
                i+=1
            mx = max(mx,pref[j+1]-pref[i])
    

        return mx

        