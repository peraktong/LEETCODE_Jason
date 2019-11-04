class Solution(object):
    def selfDividingNumbers(self, left, right):
        array = []
        for i in range(left, right + 1):

            dex = 0
            len_i = len(str(i))

            for j in str(i):
                if int(j)!=0 and i%(int(j))==0:
                    dex+=1
            if dex==len_i:
                array.append(i)

        return array


model = Solution()
print(model.selfDividingNumbers(1,22))