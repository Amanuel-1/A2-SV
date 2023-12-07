class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses  = defaultdict(int)

        for winner,loser in matches:
            losses[loser]+=1
        
        answer  = [[],[]]

        for winner,loser in matches :
            if winner not in losses and winner not in answer[0]:
                answer[0].append(winner)
            if losses[loser]==1:
                answer[1].append(loser)
        
        a,b =  answer
        a = sorted(a)
        b = sorted(b)
        answer  = [a,b]
        return answer
        