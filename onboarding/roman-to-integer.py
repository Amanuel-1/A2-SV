class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0

        mp = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }


        for i in range(len(s)):
            ans +=mp[s[i]]
            
            if i==0:
                continue
            elif (s[i]=="V" or s[i] =="X") and s[i-1]=="I":
                ans-= (2*mp["I"])
            elif (s[i]=="L" or s[i]=="C") and s[i-1]=="X":
                ans-= (2*mp["X"])
            elif (s[i]=="D" or s[i]=="M") and s[i-1]=="C":
                ans-=(2*mp["C"])        


        return ans

