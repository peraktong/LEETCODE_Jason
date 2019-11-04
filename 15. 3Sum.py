nums = [-1, 0, 1, 2, -1, -4]

def three_sum(nums):

    ans = []
    # from small to big
    nums.sort()
    for i in range(0,len(nums)-2):
        if nums[i]>0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l = i+1
        r = len(nums)-1
        while l<r:
            tot = nums[i]+nums[l]+nums[r]
            if tot<0:
                l+=1
            elif tot>0:
                r-=1
            else:
                ans.append([nums[i],nums[l],nums[r]])
                while l<r and nums[l]==nums[l+1]:
                    l+=1
                while l<r and nums[r]==nums[r-1]:
                    r-=1
                l+=1
                r-=1
    return ans


print(three_sum(nums=nums))