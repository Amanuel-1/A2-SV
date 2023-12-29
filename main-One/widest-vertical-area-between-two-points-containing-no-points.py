class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points  = sorted(points, key =lambda x:x[0])
        mx_dist  = 0

        for i in range(len(points)-1):
            mx_dist  = max(mx_dist,points[i+1][0]-points[i][0])



        return mx_dist

