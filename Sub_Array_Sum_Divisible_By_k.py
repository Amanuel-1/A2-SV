from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pref = defaultdict(int)
        pref[0] = 1 
        count = 0
        curr= 0

        for num in nums:
            curr = (curr+ num) % k
            count += pref[curr]
            pref[curr] += 1

        return count
