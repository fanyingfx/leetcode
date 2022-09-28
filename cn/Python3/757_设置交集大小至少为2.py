# @algorithm @lc id=759 lang=python3 
# @title set-intersection-size-at-least-two

from typing import Optional
from cn.Python3.mod.preImport import *
# @test([[1,3],[1,4],[2,5],[3,5]])=3
# @test([[1,2],[2,3],[2,4],[4,5]])=5
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int: