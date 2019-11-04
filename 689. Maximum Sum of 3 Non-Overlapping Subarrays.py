nums = [1,2,1,2,6,7,5,1]

k=2
def ans(nums,k):
    w = []

    for i in range(k-1,len(nums)):
        w.append(sum(nums[i-k+1:i+1]))
    # Here w is the max window at i th node:
    # i>=k-1:
    left = [0] * len(w)
    best = 0
    # Here left means the left subarray and we update the values when
    # we find...
    # Here left,right and best are indexes
    for i in range(len(w)):
        if w[i]>w[best]:
            best =i
        left[i]=best

    right = [0]*len(w)
    best=len(w)-1
    # Here we want 1-2 not 2-1
    for i in range(len(w)-1,-1,-1):
        if w[i]>=w[best]:
            best=i
        right[i] = best

    ans = None
    for b in range(k,len(w)-k):
        a,c = left[b-k],right[b+k]
        if ans is None or (w[a]+w[b]+w[c])>(w[ans[0]]+w[ans[1]]+w[ans[2]]):
            ans=a,b,c
    print(ans)
    return ans






    return None


ans(nums,k)