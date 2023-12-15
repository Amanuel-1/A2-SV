class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

        for a in arr:
            if arr.count(a)/len(arr) >0.25:
                return a
                



        