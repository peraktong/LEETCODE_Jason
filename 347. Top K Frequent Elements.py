nums = [1,1,1,2,2,3]
k = 2
dic = {}
for i in nums:
    dic[i]=dic.get(i,0)+1
dic = sorted(dic.items(),key=lambda x:x[1],reverse=True)
print(dic)
ans = [x[0] for x in dic[:k]]
print(ans)
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dic = {}
        for i in nums:
            dic[i]=dic.get(i,0)+1
        dic = sorted(dic.items(),key=lambda x:x[1],reverse=True)
        return [x[0] for x in dic[:k]]
        

"""
