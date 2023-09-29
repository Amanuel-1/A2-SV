from collections import defaultdict
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        canreach = set()

        for (a,b) in edges:
            graph[a].append(b)
            canreach.add(b)
        ans=[]
        for i in range(n):
            if i not in canreach:
                ans.append(i)
        return ans

        
