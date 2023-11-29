class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        num  = abs(x)
        k = 10
        newnum = 0

        if x<0:
            return False
        else:

            while x>=10:
                newnum  = newnum*10 +  x%10
                x//=10
            
            newnum  = newnum*10 +  x%10
            print(newnum)

            return num ==newnum


        