from collections import defaultdict

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mp = defaultdict(list)
        mn = float('inf')
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    mn = min(mn, i + j)
                    mp[i + j].append(list1[i])

        return mp[mn]