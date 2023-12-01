class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minlen  = min(len(word1),len(word2))
        result  = ""
        for i in range(minlen):
            result+= (word1[i] + word2[i])
        
        result+= word1[minlen:]
        result+= word2[minlen:]


        return result


        