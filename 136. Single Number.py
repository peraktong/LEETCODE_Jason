nums = [4,1,2,1,2]
#nums=[1,0,1]
#nums = [2,2,1]
ans = {}
for i in nums:

    try:
        ans.pop(i)
    except:
        ans[i]=1
print(ans.popitem()[0])






