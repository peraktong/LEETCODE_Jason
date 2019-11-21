
class Solution:
    def largestNumber(self, nums):

        r = ''.join(sorted(map(str, nums), cmp = lambda x, y: [1, -1][x + y > y + x]))
        print(r)
        return r

model = Solution()
model.largestNumber(nums=[3,30,34,5,9])