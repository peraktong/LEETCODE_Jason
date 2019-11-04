
from _heapq import heappush,heappop
#from queue import  PriorityQueue
target = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]

heap_array = []
for i in target:
    heappush(heap_array,i)
ans = [heappop(heap_array) for i in range(len(heap_array))]


# print(ans)

"""

target2 = {ans[i]:target[i] for i in range(len(target))}
print(target2)]
"""


