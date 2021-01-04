#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k,hs,max_length=-1,{},0
       
        for idx,c in enumerate(s):
            if c in hs and hs[c]>k:
                k = hs[c]
            hs[c]=idx
            max_length=max(max_length,idx-k)

        return max_length

# @lc code=end

