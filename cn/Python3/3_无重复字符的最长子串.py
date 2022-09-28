# @algorithm @lc id=3 lang=python3 
# @title longest-substring-without-repeating-characters
from cn.Python3.mod.preImport import *
# @test("abcabcbb")=3
# @test("bbbbb")=1
# @test("pwwkew")=3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0
        max_length=0
        d={}
        for i in range(len(s)):
            if s[i] not in d or d[s[i]]<start:
                max_length=max(max_length,i-start+1)
            else:
                start=d[s[i]]+1
            d[s[i]]=i
        
        return max_length 