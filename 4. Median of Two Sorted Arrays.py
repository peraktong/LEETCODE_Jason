import numpy as np
x = [1,2,3,4,6]
y = [4,9,10]

x = [1,3]
y=[2]

def median(x,y):
    length = len(x)+len(y)
    while len(x)>1 and len(y)>1:
        if x[0]>y[0]:
            y.remove(y[0])
        else:
            x.remove(x[0])


        if x[-1]>y[-1]:
            x.remove(x[-1])
        else:
            y.remove(y[-1])

        length -= 2
    temp = x+y
    while len(temp)>2:
        temp.pop(temp[0])
        temp.pop(temp[-1])

    return sum(temp)/len(temp)


output = median(x,y)
print(output)
print(np.median(x+y))

"""
class Solution:

    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n,A,B = len(nums1),len(nums2),nums1,nums2
        if m>n:
            m,n,A,B = n,m,B,A
        if n==0:
            return None
        # assume n>m:
        init_min,init_max,half_length = 0,m,(m+n+1)//2
        # half length can be either int / int +0.5
        while init_min<=init_max:
            i = (init_min+init_max)//2
            j = half_length-i
            
            if i<m and B[j-1]>A[i]:
                # we still need to seek the max of the left part
                init_min=i+1
            elif i>0 and A[i-1]>B[j]:
                # right part too big:
                init_max =i-1
            else:
                # found it
                if i==0:
                    max_left = B[j-1]
                elif j==0:
                    max_left = A[i-1]
                else:
                    max_left = max(A[i-1], B[j-1])
                # odd: median is just the biggest number of the left
                if (m + n) % 2 == 1:
                    return max_left
                
                if i==m:
                    min_right = B[j]
                elif j==n:
                    min_right = A[i]
                else:
                    min_right = min(A[i],B[j])
                return (max_left+min_right)/2.0
                
                    
        
"""


"""


class Solution:
    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        if l % 2 == 1:
            return self.kth(A, B, l // 2)
        else:
            return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.   

    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia, ib = len(a) // 2 , len(b) // 2
        ma, mb = a[ia], b[ib]

        # when k is bigger than the sum of a and b's median indices 
        if ia + ib < k:
            # if a's median is bigger than b's, b's first half doesn't include k
            if ma > mb:
                return self.kth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.kth(a[ia + 1:], b, k - ia - 1)
        # when k is smaller than the sum of a and b's indices
        else:
            # if a's median is bigger than b's, a's second half doesn't include k
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)

"""