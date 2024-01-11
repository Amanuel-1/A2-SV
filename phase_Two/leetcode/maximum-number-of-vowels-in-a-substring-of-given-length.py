class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(["a","e","i","o","u"])
        mincount  = 0

        for i in range(k):
           if s[i] in vowels:
               mincount+=1
        newcount  = mincount
        for i in range(k,len(s)):
            if s[i] in vowels:
                newcount+=1
            if s[i-k] in vowels:
                newcount-=1
            
            mincount = max(mincount,newcount)

        return mincount
        

