class Solution:
    def hammingDistance(self,x,y):
        return(bin(x^y).count("1"))

model = Solution()
print(model.hammingDistance(x=1,y=4))