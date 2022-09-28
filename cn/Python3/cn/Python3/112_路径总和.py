# @algorithm @lc id=112 lang=python3 
# @title path-sum

from typing import Optional
from cn.Python3.mod.preImport import *
# @test([5,4,8,11,null,13,4,7,2,null,null,null,1],22)=true
# @test([1,2,3],5)=false
# @test([],0)=false
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node,val):
            if not node:
                return False
            if node.left is None and node.right is None:
                return node.val==val
            return dfs(node.left,val-node.val) or dfs(node.right,val-node.val)
        return dfs(root,targetSum)
