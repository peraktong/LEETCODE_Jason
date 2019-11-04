import math
import bisect
l=1
r=15

threes = []
fives = []
num=1
while num<=r:
    threes.append(num)
    num*=3

num=1
while num<=r:
    fives.append(num)
    num*=5
ans =0
for i in range(len(fives)):
    left = l//fives[i]
    right = math.ceil(r/fives[i])
    ans+=bisect.bisect_right(threes,right)-bisect.bisect_left(threes,left)
print(ans)
