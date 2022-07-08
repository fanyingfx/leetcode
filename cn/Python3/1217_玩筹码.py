# @algorithm @lc id=1329 lang=python3 
# @title minimum-cost-to-move-chips-to-the-same-position


from cn.Python3.mod.preImport import *
# @test([1,2,3])=1
# @test([2,2,2,3,3])=2
# @test([1,1000000000])=1
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        l=[0,0]
        for coin in position:
            l[coin&1]+=1
        return min(l[0],l[1])