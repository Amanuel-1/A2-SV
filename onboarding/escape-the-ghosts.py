class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:

        ghost_arrival  = float('inf')
        

        for x,y in ghosts:
            dx,dy  = abs(x-target[0]), abs(y-target[1])
            if (dx+dy)<= (abs(target[0])+ abs(target[1])):
                return False

            
        

        return True
