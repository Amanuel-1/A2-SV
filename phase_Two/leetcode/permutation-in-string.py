class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ans = []
        mp = defaultdict(int)
        m = defaultdict(int)
        if len(s1)>len(s2):
            return []
                
        ls, lp = len(s2), len(s1)
        for i in range(lp):
            m[s1[i]] += 1
            mp[s2[i]] += 1
        
        for i in range(lp, ls):
            if m == mp  :
                ans.append(i - lp)
            mp[s2[i]] += 1
            mp[s2[i - lp]] -= 1
            if mp[s2[i - lp]] == 0:
                del mp[s2[i - lp]]
        if mp==m  and len(m)==len(mp):
            ans.append(len(s2)-lp)
            
        return ans
        