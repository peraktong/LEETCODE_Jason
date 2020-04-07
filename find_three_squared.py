# find all a^2+b^2=c^2 in an array, include negative

nums = [-5,-3,-1,0,2,3,4,5,6,-8,10]



def helper(nums):
    nums = sorted(nums, key=lambda x: x ** 2)
    ans = []
    if len(nums)<3:
        return []
    N = len(nums)
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                temp = nums[i]**2+nums[j]**2-nums[k]**2
                if temp==0:
                    ans.append([nums[i],nums[j],nums[k]])
                elif temp<0:
                    break
    return ans
an1 = helper(nums)
"""


# trade-off between space and time
from collections import OrderedDict

def helper2(nums):
    nums = sorted(nums, key=lambda x: x ** 2)
    ans = []
    if len(nums)<3:
        return []
    N = len(nums)
    dic = OrderedDict()
    for i in range(N-2):
        for j in range(i+1,N-1):
            temp = nums[i]**2+nums[j]**2
            if temp in dic:
                dic[temp].append([i, j])
            else:
                dic[temp] = []
            for k in range(j+1,N):
                if nums[k]**2 in dic:
                    for p in dic[nums[k]**2]:
                        ans.append([nums[p[0]],nums[p[1]],nums[k]])
                if nums[k]**2>temp:
                    break
    return ans
an2 = helper2(nums)

"""



