class TreeNode():
    def __init__(self,x):
        self.value = x
        self.left = None
        self.right = None



class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # check if there is no array
        if not nums:
            return None
        max_index = nums.index(max(nums))
        node = TreeNode(nums[max_index])
        node.left = self.constructMaximumBinaryTree(nums[:max_index])
        node.right = self.constructMaximumBinaryTree(nums[max_index + 1:])

        return node

model = Solution()
model.constructMaximumBinaryTree(nums=[3,2,1,6,0,5])