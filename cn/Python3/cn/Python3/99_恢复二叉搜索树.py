# @algorithm @lc id=99 lang=python3 
# @title recover-binary-search-tree


from typing import Optional
from cn.Python3.mod.preImport import *
# @test([1,3,null,null,2])=[3,1,null,null,2]
# @test([3,1,4,null,null,2])=[2,1,4,null,null,3]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        a,b=None,None
        res=[]
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            res.append(node)
            inorder(node.right)
        inorder(root)
        prev=res[0]
        l=[n.val for n in res]
        for n in res:
            if n.val<prev.val:
                if not a:
                    a=prev
                    b=n
                else:
                    b=n
            prev=n
        a.val,b.val=b.val,a.val
            
            

            