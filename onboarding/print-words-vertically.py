class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        n = len(max(words, key=len))
        answer = [""] * n

        for j in range(len(words)):
            for i in range(n):
                if i < len(words[j]):
                    answer[i] += words[j][i]
                else:
                    answer[i] += " "

        for i in range(n):
            answer[i] = answer[i].rstrip()

        return answer