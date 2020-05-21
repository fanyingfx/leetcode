#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3:
            return []
        res = set()
        nums.sort()
        for index,a in enumerate(nums[:-2]):
            if index > 1 and a==nums[index-1]:
                continue
            d ={}
            for b in nums[index+1:]:
                if b not in d:
                    d[-a-b]=1
                else:
                    res.add((a,-a-b,b))
        return list(map(list,res))
                
sln = Solution()

print(sln.threeSum([-1,0,1,2,-1,-4]))

# @lc code=end

