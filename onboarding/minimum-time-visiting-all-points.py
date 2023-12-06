class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total =0
        for i in range(len(points)-1):
            dx,dy  = abs(points[i+1][0]-points[i][0]) ,abs(points[i+1][1] - points[i][1])
            total += ( min(dx,dy) + abs(dy-dx) )
        

        return total