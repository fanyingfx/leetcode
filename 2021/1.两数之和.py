#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for index,num in enumerate(nums):
            other = target-num
            if other in d:
                return [index,d[other]]
            else:
                d[num]=index
        return [-1,-1]
# @lc code=end

