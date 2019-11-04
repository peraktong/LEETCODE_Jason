class Solution(object):
    def diStringMatch(self, S):
        low,high = 0,len(S)
        re = []
        for x in S:
            if x=="I":
                re.append(low)
                low+=1
            else:
                re.append(high)
                high-=1
        # high==low
        return re+[low]


model = Solution()
print(model.diStringMatch(S="DDI"))