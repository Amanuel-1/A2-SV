class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        sum_ =0
        for i in range(min(start,destination), max(start,destination)):
            sum_+=distance[i]
        

        return min(sum(distance)-sum_,sum_)

        