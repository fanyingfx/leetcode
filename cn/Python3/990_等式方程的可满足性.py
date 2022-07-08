# @algorithm @lc id=1032 lang=python3 
# @title satisfiability-of-equality-equations


from cn.Python3.mod.preImport import *
# @test(["a==b","b!=a"])=false
# @test(["b==a","a==b"])=true
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        d={}
        