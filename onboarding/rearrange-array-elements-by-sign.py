class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        answer =[]

        pos =[]
        neg=[]
        for n in nums:
            if n>=0:
                pos.append(n)
            else:
                neg.append(n)
        for i in range(len(pos)):
            answer.append(pos[i])
            answer.append(neg[i])

        

        return answer