# @algorithm @lc id=1 lang=python3 
# @title two-sum

import os,sys\n sys.path.append(os.getcwd())
from cn.Python3.mod.preImport import *
# @test([2,7,11,15],9)=[0,1]
# @test([3,2,4],6)=[1,2]
# @test([3,3],6)=[0,1]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: