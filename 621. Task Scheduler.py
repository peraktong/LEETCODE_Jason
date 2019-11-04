"""

import collections

tasks = ["A","A","A","B","B","B"]

from heapq import heappush, heappop
from collections import Counter
class Solution:
    def leastInterval(self, tasks, n):

        curr_time, h = 0, []
        for k,v in Counter(tasks).items():
            heappush(h, (-1*v, k))
        while h:
            i, temp = 0, []
            while i <= n:
                curr_time += 1
                if h:
                    x,y = heappop(h)
                    if x != -1:
                        temp.append((x+1,y))
                if not h and not temp:
                    break
                else:
                    i += 1
            for item in temp:
                heappush(h, item)
        return curr_time

model = Solution()
print(model.leastInterval(tasks=tasks,n=2))

"""
n=2
tasks = ["A","A","A","B","B","B"]
count_array = {}
for i in tasks:
    count_array[i] = count_array.get(i,0)+1

"""
order = sorted(count_array.items(),key=lambda k:k[1],reverse=True)
order =[i[0] for i in order]

"""
M = max(count_array.values())
max_num=0
for k in count_array.items():
    print(k)
    if k[1]==M:
        max_num+=1
print(max_num)
ans = max(len(tasks), (M - 1) * (n + 1) + max_num)

print(ans)



