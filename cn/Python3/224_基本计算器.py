# @algorithm @lc id=224 lang=python3 
# @title basic-calculator

from typing import Optional
from cn.Python3.mod.preImport import *
# @test("1 + 1")=2
# @test(" 2-1 + 2 ")=3
# @test("(1+(4+5+2)-3)+(6+8)")=23
class Solution:
    def calculate(self, s: str) -> int: