# @algorithm @lc id=124 lang=python3 
# @title binary-tree-maximum-path-sum

from typing import Optional
from cn.Python3.mod.preImport import *
# @test([1,2,3])=6
# @test([-10,9,20,null,null,15,7])=42
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int: