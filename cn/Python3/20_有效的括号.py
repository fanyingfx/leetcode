# @algorithm @lc id=20 lang=python3 
# @title valid-parentheses


from cn.Python3.mod.preImport import *
# @test("()")=true
# @test("()[]{}")=true
# @test("(]")=false
class Solution:
    def isValid(self, s: str) -> bool: