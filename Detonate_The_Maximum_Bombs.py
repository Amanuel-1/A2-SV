from collections import defaultdict
import math

class Solution:
    def maximumDetonation(self, bombs):
        mx = 1
        graph = defaultdict(list)

        def inrange(b1, b2):
            return math.sqrt((b1[0]-b2[0])**2 + (b1[1]-b2[1])**2) <= b1[2]

        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i != j and inrange(bombs[i], bombs[j]):
                    bomb_i = tuple(bombs[i] + [i])
                    bomb_j = tuple(bombs[j] + [j]) 
                    graph[bomb_i].append(bomb_j)

        def detonate(bomb, states):
            if tuple(bomb) in states:
                return 0
            if not bomb:
                return 0
            
            states.add(tuple(bomb))
            total = 1
            for bmb in graph[tuple(bomb)]:
                total += detonate(bmb, states)

            return total

        for i, bomb in enumerate(bombs):
            bomb_with_index = tuple(bomb + [i])
            states = set()
            mx = max(mx, detonate(bomb_with_index, states))

        return mx
