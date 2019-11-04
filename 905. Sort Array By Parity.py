class Solution(object):
    def sortArrayByParity(self, A):
        A.sort(key = lambda x: x % 2)
        # for x in A: print(x%2)
        return A


model = Solution()
print(model.sortArrayByParity(A = [3,1,2,4]))