class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      prefix =  strs[0]
      current_prefix = ""
      for word in strs:
        for i in range(min(len(prefix),len(word))):
          if word[i]==prefix[i]:
            current_prefix += word[i]
          else:
            break
        prefix = current_prefix
        current_prefix =""

      
      return prefix