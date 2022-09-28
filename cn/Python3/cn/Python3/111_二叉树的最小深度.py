# @algorithm @lc id=111 lang=python3 
# @title minimum-depth-of-binary-tree


from cn.Python3.mod.preImport import *
# @test([3,9,20,null,null,15,7])=2
# @test([2,null,3,null,4,null,5,null,6])=5
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def min_depth(node):
            if node.left is None and node.right is None:
                return 1
            if node.left is None:
                return min_depth(node.right)+1
            elif node.right is None:
                return min_depth(node.left)+1
            return min(min_depth(node.left),min_depth(node.right))+1
        if not root:
            return 0
        return min_depth(root)