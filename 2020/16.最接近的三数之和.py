#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums)< 3:
            return None
        nums.sort()
        res = nums[0]+nums[1]+nums[2]
        for ind in range(1,len(nums)-1):
            start_index,end_index = 0,len(nums)-1
            while start_index <ind and end_index>ind:
                curr_sum=sum((nums[start_index],nums[ind],nums[end_index]))
                if curr_sum > target:
                    end_index-=1
                elif curr_sum < target:
                    start_index += 1
                else:
                    return target
                if abs(curr_sum-target)<abs(res-target):
                    res = curr_sum
        return res

sln = Solution()

print(sln.threeSumClosest([-1,2,1,-4],1))

# @lc code=end

