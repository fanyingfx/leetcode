# @algorithm @lc id=1000037 lang=python3 
# @title get-kth-magic-number-lcci

from typing import Optional
from cn.Python3.mod.preImport import *
# @test(5)=9
class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        dp,a,b,c=[1]*(k+1),0,0,0
        for i in range(1,k):
            n1,n2,n3=dp[a]*3,dp[b]*5,dp[c]*7
            dp[i]=min(n1,n2,n3)
            if dp[i]==n1: a+=1
            if dp[i]==n2: b+=1
            if dp[i]==n3: c+=1
        return dp[k-1]