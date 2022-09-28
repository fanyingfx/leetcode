# @algorithm @lc id=100 lang=python3 
# @title same-tree


from cn.Python3.mod.preImport import *
# @test([1,2,3],[1,2,3])=true
# @test([1,2],[1,null,2])=false
# @test([1,2,1],[1,1,2])=false
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if not p.val==q.val:
            return False
        if not self.isSameTree(p.left,q.left):
            return False
        if not self.isSameTree(p.right,q.right):
            return False
        
        return True