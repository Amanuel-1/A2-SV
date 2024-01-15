from collections import defaultdict
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        mp = defaultdict(int)
        m = defaultdict(int)
        if len(p)>len(s):
            return []
                
        ls, lp = len(s), len(p)
        for i in range(lp):
            m[p[i]] += 1
            mp[s[i]] += 1
        
        for i in range(lp, ls):
            if m == mp :
                ans.append(i - lp)
            mp[s[i]] += 1
            mp[s[i - lp]] -= 1
            if mp[s[i - lp]] == 0:
                del mp[s[i - lp]]
        if mp==m :
            ans.append(len(s)-lp)
            
        return ans