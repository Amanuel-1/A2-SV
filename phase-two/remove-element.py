class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        mp = defaultdict(int)
        n = len(nums)
        vec = nums[:]
        nums.clear()
        for i in range(len(vec)):
            mp[vec[i]] += 1
            if vec[i] != val:
                nums.append(vec[i])
        
        return n - mp[val]