class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.data = [sum(nums[:x]) for x in range(len(nums) + 1)]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        # print(self.data)
        return self.data[j + 1] - self.data[i]

    # Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)