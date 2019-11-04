nums = [-2,1,-3,4,-1,2,1,-5,4]

def sort(nums):
    # greedy:
    # max_global and current max:
    # What you need to know is that we need at least N in time complexity:
    n = len(nums)
    curr_sum = max_sum = nums[0]
    for i in range(1, n):
        curr_sum = max(nums[i], curr_sum + nums[i])
        max_sum = max(max_sum, curr_sum)

    return max_sum

def sort_DP(nums):
    n = len(nums)
    max_sum = nums[0]
    # Let's update the nums array:
    for i in range(1,n):
        if nums[i-1]>0:
            # Here num[i-1] means the current max at that step, which is updated previously
            nums[i]+=nums[i-1]
            max_sum = max(max_sum,nums[i])
    return max_sum

print(sort(nums=nums))
print(sort_DP(nums=nums))