from collections import defaultdict

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    graph[i+1].append(j+1)

        provinces = 0
        visited = set()

        def search(city):
            nonlocal provinces
            if city not in graph:
                return
            else:
                visited.add(city)
                
                for c in graph[city]:
                    if c not in visited:
                        search(c)

        for c in graph:
            if c not in visited:
                search(c)
                provinces += 1 

        return provinces
