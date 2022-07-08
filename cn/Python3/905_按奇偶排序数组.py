# @algorithm @lc id=941 lang=python3 
# @title sort-array-by-parity


import re
from cn.Python3.mod.preImport import *
# @test([3,1,2,4])=[2,4,3,1]
# @test([0])=[0]
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left,right=0,0
        while right<len(nums):
            if nums[right] % 2 == 0:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
            right+=1
        return nums