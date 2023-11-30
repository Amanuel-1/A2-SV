class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if (num-3)%3==0:
            start  = (num-3)//3

            return [start,start+1,start+2]
        return []