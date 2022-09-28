# @algorithm @lc id=42 lang=python3 
# @title trapping-rain-water


from cn.Python3.mod.preImport import *
# @test([0,1,0,2,1,0,1,3,2,1,2,1])=6
# @test([4,2,0,3,2,5])=9
class Solution:
    def trap(self, height: List[int]) -> int: