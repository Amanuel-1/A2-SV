from collections import defaultdict
n= int(input())
graph = defaultdict(list)
for _ in range(int(input())):
    opr = list(map(int,input().split()))

    if opr[0] ==1:
        graph[opr[1]].append(opr[2])
        graph[opr[2]].append(opr[1])
    else:
        print(*graph[opr[1]])
