from collections import defaultdict
for _ in range(int(input())):
    row = list(map(int,input().split()))
    edges =[]
    for e in range(len(row)):
        if row[e] ==1:
            edges.append(e+1)

    print(len(edges),*(edges))
