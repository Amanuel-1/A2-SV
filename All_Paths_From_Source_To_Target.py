class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        answer=[]
        dest = len(graph)-1

        def search(ind,arr):
            if ind==dest:
                answer.append(arr+[dest])
                return
            
            for node in graph[ind]:
                               
                search(node,arr+[ind])

        search(0,[])
        return answer
