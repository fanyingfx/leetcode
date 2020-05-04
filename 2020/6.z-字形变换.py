#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        length = len(s)-1

        for i in range(1,numRows+1):
            for j in range(0,length,2*step-2):


# @lc code=end

