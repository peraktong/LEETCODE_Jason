

#
def rain_water(x):
    height = []
    left=0
    right=0
    ans = 0

    for i in x:
        left = max(left,i)
        height.append(left)
    height.reverse()
    for i,val in enumerate(reversed(x)):
        right = max(right,val)
        ans+=min(height[i],right)-val
    print(ans)
    return ans
x = [0,1,0,2,1,0,1,3,2,1,2,1]
rain_water(x=x)