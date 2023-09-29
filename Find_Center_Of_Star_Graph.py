from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for (a,b) in edges:
            graph[a].append(b)
            graph[b].append(a)
        print(graph)

        for e in graph:
            if len(graph[e])>1:
                return e
        return -1

        
