"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from collections import defaultdict
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        graph  = defaultdict(Employee)

        for e in employees:
            graph[e.id] =e
        
        ans = graph[id].importance
        

        def explore(emp):
            nonlocal ans            
            if not emp:
                return
            if not emp.subordinates:
                return
            else:
                for eid in emp.subordinates:
                    ans+=graph[eid].importance
                    explore(graph[eid])
        explore(graph[id])
        return ans
        


        
        
