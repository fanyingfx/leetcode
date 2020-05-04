
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# https://leetcode-cn.com/problems/reverse-integer/description/
#
# algorithms
# Easy (33.38%)
# Likes:    1748
# Dislikes: 0
# Total Accepted:    300.3K
# Total Submissions: 887.2K
# Testcase Example:  '123'
#
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 
# 示例 1:
# 
# 输入: 123
# 输出: 321
# 
# 
# 示例 2:
# 
# 输入: -123
# 输出: -321
# 
# 
# 示例 3:
# 
# 输入: 120
# 输出: 21
# 
# 
# 注意:
# 
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
# 
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        pos_max_int = 2**31-1
        neg_max_int = -2**31
        flag = x< 0
        x = abs(x)
        while x > 9:
            curr_val = x % 10
            res= res * 10 + curr_val
            x = x //10
        if flag:
            res = -res
            x = -x
        print(res)
        if res > pos_max_int//10 or (res==pos_max_int//10 and x > 7):
            return 0
        if res < int(neg_max_int/10) or(res==neg_max_int//10 and x < -8):
            return 0
        
        return res * 10 + x
sln = Solution()        
print(sln.reverse(-1563847412))
# @lc code=end

