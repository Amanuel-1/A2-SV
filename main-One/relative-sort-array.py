class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mp   = defaultdict(int)
        for i in range(len(arr2)):
            mp[arr2[i]] = i

        def comp(x):
            if x in mp:
                return mp[x]
            else:
                return len(arr1)+x

        arr1 = sorted(arr1,key=comp)

        return arr1