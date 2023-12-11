class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        mp  = defaultdict(int)
        rows = ["qwertyuiop","asdfghjkl","zxcvbnm"]
        answer  = []
        for r in range(len(rows)):
            for c in rows[r]:
                mp[c]=r
        

        for word in words:
            w  = word.lower()
            row  =mp[w[0]]
            for c in w:
                if mp[c]!=row:
                    row=mp[c]
                    break
            if row==mp[w[0]]:
                answer.append(word)
    
        return answer
            
                




        
        