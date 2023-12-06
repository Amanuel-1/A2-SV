class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest =-1
        for i in range(len(num)-2):
            if num[i]==num[i+1]==num[i+2]:
                largest =  max(largest, int(num[i]))
        
        return str(largest)*3 if largest != -1 else ""      