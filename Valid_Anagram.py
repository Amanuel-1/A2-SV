from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      map_s = Counter(s)
      map_t = Counter(t)
      if len(map_s) != len(map_t):
        return False
      for i in list(set(s)):
        if map_s[i] != map_t[i]:
          return False
      
      return True

