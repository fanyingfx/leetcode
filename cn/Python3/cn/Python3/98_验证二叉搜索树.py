# @algorithm @lc id=98 lang=python3 
# @title validate-binary-search-tree


from typing import Optional
from cn.Python3.mod.preImport import *
# @test([2,1,3])=true
# @test([5,1,4,null,null,3,6])=false
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def helper(node,lower,upper):
    if not node:
        return True
    val=node.val
    if val<=lower or val>=upper:
        return False
    if not helper(node.left,lower,val):
        return False
    if not helper(node.right,val,upper):
        return False
    return True
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return helper(root,float('-inf'),float('inf'))