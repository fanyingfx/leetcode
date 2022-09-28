# @algorithm @lc id=226 lang=python3 
# @title invert-binary-tree

from typing import Optional
from cn.Python3.mod.preImport import *
# @test([4,2,7,1,3,6,9])=[4,7,2,9,6,3,1]
# @test([2,1,3])=[2,3,1]
# @test([])=[]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def invert(node):
    if node is None:
        return
    else:
        node.left,node.right=node.right,node.left
        invert(node.left)
        invert(node.right)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        invert(root) 
        return root
       