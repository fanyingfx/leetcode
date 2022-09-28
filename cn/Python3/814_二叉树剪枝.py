# @algorithm @lc id=832 lang=python3 
# @title binary-tree-pruning

from typing import Optional
from cn.Python3.mod.preImport import *
# @test([1,null,0,0,1])=[1,null,0,null,1]
# @test([1,0,1,0,0,0,1])=[1,null,1,null,1]
# @test([1,1,0,1,1,0,1,0])=[1,1,0,1,1,null,1]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right 
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node:Optional[TreeNode]):
            if not node:
                return 0
            left_val=0
            left_val+=dfs(node.left)
            if left_val==0:
                node.left=None
            right_val=0
            right_val+=dfs(node.right)
            if right_val==0:
                node.right=None
            return left_val+node.val+right_val
        
        res_val=dfs(root)
        if res_val==0:
            return None
        return root