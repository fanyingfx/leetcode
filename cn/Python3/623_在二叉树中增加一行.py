# @algorithm @lc id=623 lang=python3 
# @title add-one-row-to-tree

from typing import Optional
from cn.Python3.mod.preImport import *
# @test([4,2,6,3,1,5],1,2)=[4,1,1,2,null,null,6,3,1,5]
# @test([4,2,null,3,1],1,3)=[4,2,null,1,1,3,null,null,1]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]: