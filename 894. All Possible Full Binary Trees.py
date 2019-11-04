"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    memory = {0:[],1:[TreeNode(0)]}
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N not in self.memory:
            ans = []
            for x in range(0,N):
                y = N-1-x
                for left in self.allPossibleFBT(N=x):
                    for right in self.allPossibleFBT(N=y):
                        bins = TreeNode(0)
                        bins.left = left
                        bins.right = right
                        ans.append(bins)
            self.memory[N] = ans
        return self.memory[N]










"""