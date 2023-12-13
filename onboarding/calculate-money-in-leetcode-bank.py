class Solution:
    def totalMoney(self, n: int) -> int:

        weeks  =  n//7
        rem = n%7
        answer  =((rem *(2*(weeks+1)+ (rem-1)))//2)

        if n>7:

            answer = (weeks *(2*28 + (weeks-1)*7))//2  + ((rem *(2*(weeks+1)+ (rem-1)))//2)

        return answer