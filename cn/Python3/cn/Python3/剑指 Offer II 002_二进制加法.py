# @algorithm @lc id=1000231 lang=python3 
# @title JFETK5


from cn.Python3.mod.preImport import *
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]