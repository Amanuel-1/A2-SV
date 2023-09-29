from collections import defaultdict
roads =0
graph = defaultdict(list)
for a in range(int(input())):
    row = list(map(int,input().split()))


    
    for b in range(len(row)):
        if row[b] ==1:
            graph[a+1].append(b+1)

visited  = set()
for g in graph:
    visited.add(g)

    for e in graph[g]:
        if e not in visited:
            roads+=1
print(roads)
