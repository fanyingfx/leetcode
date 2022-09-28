# @algorithm @lc id=101 lang=python3 
# @title symmetric-tree


from cn.Python3.mod.preImport import *
from typing import Optional
# @test([1,2,2,3,4,4,3])=true
# @test([1,2,2,null,3,null,3])=false
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def checkSymetric(left,right):
            if left is None and right is None:
                return True
            elif left is None or right is None:
                return False
            if left.val != right.val:
                return False
            if not checkSymetric(left.left,right.right):
                return False
            if not checkSymetric(left.right,right.left):
                return False
            return True
        if not root:
            return True
        return checkSymetric(root.left,root.right)