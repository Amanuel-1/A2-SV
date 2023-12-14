class Solution:
    def largestOddNumber(self, num: str) -> str:
        answer =""
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2:
                answer = num[:i+1]
                break
        

        return answer

        