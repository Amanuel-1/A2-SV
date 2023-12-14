class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
      spaces_added = 0
      new  =""
      j=0
      for i in range(len(s)):
        
        if j<len(spaces) and i == spaces[j]:
          new += " "+s[i]
          j+=1
        else:
          new += s[i]
        
        
      
      return new