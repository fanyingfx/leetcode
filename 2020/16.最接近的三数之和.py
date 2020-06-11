#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums)<3:
            return -1
        nums.sort()
        res = nums[0]+nums[1]+nums[2]
        i = 1
        while i < len(nums):
            start,end=0,len(nums)-1
            while start< i and i < end:
                threeSum=nums[start]+nums[i]+nums[end]
                # print(start,end,i,threeSum)
                if abs(threeSum-target) < abs(res-target):
                    res=threeSum
                if threeSum > target:
                    end -=1
                elif threeSum < target:
                    start +=1
                else:
                    return threeSum
            i+=1
        return res

sln=Solution()
print(sln.threeSumClosest([-1,2,1,-4],1))


# @lc code=end

