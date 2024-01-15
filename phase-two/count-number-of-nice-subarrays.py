class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_odd = [0] * (n + 1)
        prefix_odd[0] = 0
        for i in range(1, n + 1):
            prefix_odd[i] = prefix_odd[i - 1] + (nums[i - 1] & 1)
        res = 0
        cnt = defaultdict(int)
        cnt[0] = 1
        for i in range(1, n + 1):
            res += cnt[prefix_odd[i] - k]
            cnt[prefix_odd[i]] += 1
        
        return res