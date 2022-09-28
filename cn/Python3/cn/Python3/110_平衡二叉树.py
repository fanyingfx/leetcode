# @algorithm @lc id=110 lang=python3 
# @title balanced-binary-tree


from cn.Python3.mod.preImport import *
# @test([3,9,20,null,null,15,7])=true
# @test([1,2,2,3,3,null,null,4,4])=false
# @test([])=true
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool: