# @algorithm @lc id=565 lang=python3 
# @title array-nesting

from typing import Optional
from cn.Python3.mod.preImport import *
# @test([5,4,0,3,1,6,2])=4
# @test([0,1,2])=1
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        nums=nums.copy()
        curr_len=0
        max_len=0
        s=set()
        arr_len=len(nums)
        unused=set(range(arr_len))
        i=0
        while unused:
            if i not in s:
                s.add(i)
                curr_len+=1
                max_len=max(curr_len,max_len)
                unused.remove(i)
                i=nums[i]
            else:
                s.clear()
                curr_len=0
                i=unused.pop()
                unused.add(i)
        return max_len
                
            
