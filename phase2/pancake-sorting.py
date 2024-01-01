class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        temp = sorted(arr, reverse = True)
        ans = []
        for num in temp:
            index = arr.index(num)
            ans.append(index+1)
            ans.append(n)
            arr[:index+1] = reversed(arr[:index+1])
            arr[:n] = reversed(arr[:n])
            n-=1
        return ans