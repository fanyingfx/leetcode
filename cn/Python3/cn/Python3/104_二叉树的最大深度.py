# @algorithm @lc id=104 lang=python3 
# @title maximum-depth-of-binary-tree


from cn.Python3.mod.preImport import *
# @test([3,9,20,null,null,15,7])=3
# @test([1,null,2])=2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int: