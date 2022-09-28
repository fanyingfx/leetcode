# @algorithm @lc id=113 lang=python3 
# @title path-sum-ii

from typing import Optional
from cn.Python3.mod.preImport import *
# @test([5,4,8,11,null,13,4,7,2,null,null,5,1],22)=[[5,4,11,2],[5,8,4,5]]
# @test([1,2,3],5)=[]
# @test([1,2],0)=[]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res=[]
        def dfs(node,val,l):
            if node is None:
                return 
            if node.left is None and node.right is None:
                if node.val==val:
                    l.append(node.val)
                    res.append(l)
                return
            l.append(node.val)
            ll=l.copy()
            lr=l.copy()
            dfs(node.left,val-node.val,ll)
            dfs(node.right,val-node.val,lr)
        x=[]
        dfs(root,targetSum,x)
        return res
