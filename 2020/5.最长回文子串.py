#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (27.98%)
# Likes:    1845
# Dislikes: 0
# Total Accepted:    201.7K
# Total Submissions: 699.2K
# Testcase Example:  '"babad"'
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 
# 示例 1：
# 
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 
# 
# 示例 2：
# 
# 输入: "cbbd"
# 输出: "bb"
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0 or len(s)==1:
            return s
        if len(s)==2:
            if s[0]==s[1]:
                return s
            else :return s[0]

        max_length = (0,0,1)

        for i in range(len(s)-1):
            left,right =i,i
            while left > 0 and right < len(s) -1:
                if s[left-1] ==s[right+1]:
                    left = left -1
                    right = right +1
                    if right -left+1 > max_length[-1]:
                        max_length = (left,right,right-left+1)
                else: break
            
            if i+1 < len(s)  and s[i]==s[i+1]:
                left,right =i,i+1
                if right -left+1 > max_length[-1]:
                    max_length = (left,right,right-left+1)
                while left > 0 and right < len(s) -1:
                    if s[left-1] ==s[right+1]:
                        left = left -1
                        right = right +1
                        if right -left +1> max_length[-1]:
                            max_length = (left,right,right-left+1)
                    else:break
        print(max_length)
        left,right,_ = max_length
        return s[left:right+1]

sln = Solution()

s1 ='abb'
print(sln.longestPalindrome(s1))



# @lc code=end

