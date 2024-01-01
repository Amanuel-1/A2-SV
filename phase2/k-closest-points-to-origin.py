class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []

        points.sort(key=lambda a: a[0]**2 + a[1]**2)

        i = 0
        while i < k:
            result.append(points[i])
            i += 1

        return result