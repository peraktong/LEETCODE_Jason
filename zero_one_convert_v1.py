import heapq
from _heapq import heapify,heappop,heappush

"""
给一个数n，表示有n个0，给两个操作 ：L 表示将最左边的0变成1，C(index)表示将某个index的1变成0；
比如n =5, operations=["L","L","L","C0","L","C1"]

"""
ans = []
n=5
x = ["L","L","L","C0","L","C1"]

temp = [i for i in range(n)]
heapify(temp)
for j in range(len(x)):
    if x[j]=="L":
        heappop(temp)
    elif "C" in x[j]:
        t = int(x[j].replace("C",""))
        heappush(temp,t)

ans = [1]*n
for k in temp:
    ans[k] = 0
print(ans)



