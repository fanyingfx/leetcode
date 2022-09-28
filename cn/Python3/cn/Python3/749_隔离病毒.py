# @algorithm @lc id=750 lang=python3 
# @title contain-virus

from typing import Optional
from cn.Python3.mod.preImport import *
# @test([[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]])=10
# @test([[1,1,1],[1,0,1],[1,1,1]])=4
# @test([[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]])=13
class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int: