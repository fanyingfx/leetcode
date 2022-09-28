# @algorithm @lc id=773 lang=python3 
# @title logical-or-of-two-binary-grids-represented-as-quad-trees

from typing import Optional
from cn.Python3.mod.preImport import *
# @test([[0,1],[1,1],[1,1],[1,0],[1,0]],[[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]])=[[0,0],[1,1],[1,1],[1,1],[1,0]]
# @test([[1,0]],[[1,0]])=[[1,0]]
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        