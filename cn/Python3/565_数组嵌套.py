# @algorithm @lc id=565 lang=python3 
# @title array-nesting

from typing import Optional
from cn.Python3.mod.preImport import *
# @test([5,4,0,3,1,6,2])=4
# @test([0,1,2])=1
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        nums=nums.copy()
        s=set()
        unused_set=set(range(len(nums)))
        min_index=0
        max_len=0
        count=0
        arr_len=len(nums)
        curr_len=0
        i=0
        while count<=arr_len:
            print(i)
            if nums[i] not in s:
                arr_len+=1
                s.add(nums[i])
                unused_set.remove(i)
                curr_len+=1
                max_len=max(max_len,curr_len)
                i=nums.pop(i)
                min_index=min(i,min_index)

            else:
                s.clear()
                i=unused_set.pop()
                
        
        return max_len
        