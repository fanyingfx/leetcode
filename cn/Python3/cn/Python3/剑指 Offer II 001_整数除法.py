# @algorithm @lc id=1000228 lang=python3 
# @title xoh6Oh

#@test(15,2)=7
#@test(7,-3)=-2
#@test(1,1)=1
# @test(-2147483648,-1)=2147483647
from cn.Python3.mod.preImport import *
class Solution:
    def divide(self, a: int, b: int) -> int:
        sign=1
        if a>0 and b<0 or (a<0 and b>0):
            sign=-1
        a=-abs(a)
        b=-abs(b)
        count=0
        inc=1
        while a<=b:
            nb=b
            inc=1
            while nb+nb>=a:
                nb=nb+nb
                inc=inc+inc
            a=a-nb
            count+=inc
        res=count*sign
        if res>2147483647:
            res=2147483647
        return res
        