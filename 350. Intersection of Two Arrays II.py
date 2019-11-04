nums1 = [1,2,2,1]
nums2 = [2,2]

import collections

a, b = map(collections.Counter,(nums1,nums2))

print(list((a & b).elements()))