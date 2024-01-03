class Solution:
    def isPalindrome(self, s: str) -> bool:
        pure  = "".join(filter(str.isalnum,s)).lower()

        i,j = 0,len(pure)-1

        while i<j:
            if pure[i]!=pure[j]:
                return False
            else:
                i+=1
                j-=1
        print(pure)
        return True
        