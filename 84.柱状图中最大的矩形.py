#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

## @lc code=start

import sys
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        active_list = {}
        for i,h in enumerate(heights):
            active_list[i] = h
        max_area = heights[0]
        prev_high=heights[0]
        for i,h in enumerate(heights[1:]):
           pass 

## @lc code=end