class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs  = sorted(costs)
        cur  =0
        total =0

        for n in costs:
            coins-=n
            if coins>=0:
                total+=1

        return total

