from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = defaultdict(int)
        i, j = 0, 0
        max_len = 0

        while j < len(s):
            # Increase the count of the current character
            mp[s[j]] += 1

            while mp[s[j]] > 1:
               
                mp[s[i]] -= 1
                i += 1

            max_len = max(max_len, j - i + 1)
            j += 1

        return max_len