from collections import defaultdict
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        mx  = 0

        for (a,b) in roads:
            graph[a].append(b)
            graph[b].append(a)
        
        for i in range(n):
            for j in range(i+1,n):
                rank = len(graph[i])+len(graph[j])
                if i in graph[j] or j in graph[i]:
                    rank-=1
                mx = max(mx,rank)

        

        return mx

        
