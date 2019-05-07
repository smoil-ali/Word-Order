from collections import defaultdict


d = defaultdict(list)
for x in range(int(input())):
    y=input()
    d[y].append(1)

print(len(d))
for i,j in d.items():
    print(sum(j),end=" ")
