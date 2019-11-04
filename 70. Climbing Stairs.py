# each 1 or 2 steps
import math
def climb_stairs(n):

    n2 = n//2

    if n2==0:
        return 1
    ans=1
    for i in range(1,n2+1):
        n1 = n-i*2
        ans+=(math.factorial(i+n1)/math.factorial(i)/math.factorial(n1))

    return int(ans)

print(climb_stairs(n=3))