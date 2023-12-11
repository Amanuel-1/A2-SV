class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        answer =[""]*len(indices)
        for c,i in zip(s,indices):
            answer[i]=c

        return "".join(answer)