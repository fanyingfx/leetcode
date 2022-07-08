# @algorithm @lc id=450 lang=python3 
# @title delete-node-in-a-bst


from typing import Optional

from cn.Python3.mod.preImport import *
# @test([5,3,6,2,4,null,7],3)=[5,4,6,2,null,null,7] 
# @test([5,3,6,2,4,null,7],7)=[5,3,6,2,4,null]
# @test([5,3,6,2,4,null,7], 5)=[6,3,7,2,4]
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self) -> str:
        return str(self.val)
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def find_node(node,val):
            if node is None:
                return None
            if node.left is None and  node.right is None:
                return None
            if node.left is not None and node.left.val==val:
                return node
            if node.right is not None and node.right.val==val:
                return node
            new_node=find_node(node.left,val)
            if new_node is not None:
                return new_node
            new_node=find_node(node.right,val)
            return new_node
        dummy_root=TreeNode(left=root)
        
        partent_node=find_node(dummy_root,key)
        if partent_node is None:
            return root
        if partent_node.left is None or partent_node.left.val!=key:
            delete_node=partent_node.right
            if delete_node.left is not None and delete_node.right is not None:
                partent_node.right=delete_node.left
                delete_node.left.right=delete_node.right
            if delete_node.left is None:
                partent_node.right=delete_node.right
            if delete_node.right is None:
                partent_node.right=delete_node.left
        else:
            delete_node=partent_node.left
            if delete_node.left is not None and delete_node.right is not None:
                partent_node.left=delete_node.left
                delete_node.left.right=delete_node.right
            if delete_node.left is None:
                partent_node.left=delete_node.right
            if delete_node.right is None:
                partent_node.left=delete_node.left
        return dummy_root.left
        