#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right = 0,len(height) -1
        max_area = 0
        while left != right:
           if height[left] > height[right]:
               s = height[right] *(right-left)
               right -=1
           else:
               s = height[left] *(right-left)
               left +=1
           if s > max_area:max_area=s
        return max_area
     
    
sln = Solution()

print(sln.maxArea([1,8,6,2,5,4,8,3,7]))

# @lc code=end

