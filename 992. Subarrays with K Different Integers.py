import collections
def subarraysWithKDistinct(A, K):
    """
    :type A: List[int]
    :type K: int
    :rtype: int
    """
    if len(A) < K:
        return 0
    ans = 0
    # use a dictionary to save elements until this index

    count = {}
    temp = set([])
    for i in range(1, len(A) + 1):
        print(temp,count)
        temp.add(A[i - 1])
        count[i] = temp
    count[0] = set([])
    print(count)

    for i in range(len(A) + 1):
        for j in range(i):
            print(i,j,count[j],count[i])
            if len(count[i] - count[j]) == K:
                ans += 1

    return ans

print(subarraysWithKDistinct(A=[1,2,1,3,4],K=3))