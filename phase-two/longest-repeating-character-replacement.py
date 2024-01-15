from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        mxlen = 0
        mp = defaultdict(int)
        i = 0
        maxfreq = 0

        for j in range(n):
            mp[s[j]] += 1
            maxfreq  =  max(maxfreq,mp[s[j]])

            if j - i + 1 - maxfreq> k:
                mp[s[i]] -= 1
                if mp[s[i]] == 0:
                    del mp[s[i]]
                i += 1

            mxlen = max(mxlen, j - i + 1)

        return mxlen