class Solution(object):
    def pruneTreen(self,input):
        pass

model =Solution()

input = [1,None,0,0,1]
print(model.pruneTreen(input=input))

if not 1:
    print("c")

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def check(node):
            if not node:
                return False
            a1 = check(node.left)
            a2 = check(node.right)
            if not a1:
                node.left=None
            if not a2:
                node.right=None
            return node.val==1 or a1 or a2
        return root if check(root) else None
        

"""



