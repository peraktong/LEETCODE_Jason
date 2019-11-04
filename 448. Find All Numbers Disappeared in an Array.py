A = [4,3,2,7,8,2,3,1]

# brutal force:
"""

def find(nums):
    ans = [x for x in range(1, len(nums) + 1) if x not in nums]
    print(ans)
    return ans
"""


def find(nums):
    ans = list(range(1,len(nums)+1))
    # convert list to dic with no value only key
    # ans = list(dict.fromkeys(ans))
    ans = list(set(ans)-set(nums))
    print(ans)
    return ans

find(nums=A)