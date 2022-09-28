# @algorithm @lc id=22 lang=python3 
# @title generate-parentheses


from cn.Python3.mod.preImport import *
# @test(3)=["((()))","(()())","(())()","()(())","()()()"]
# @test(1)=["()"]
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n==1:
            return ["()"]
        res=[]
        def genpars(s,left,right):
            if left==0 and right==0:
                res.append(s)
                return
            if left == right:
                genpars(s+"(",left-1,right)
            else:
                if left > 0:
                    genpars(s+"(",left-1,right)
                genpars(s+")",left,right-1)
        genpars("",n,n)
        return res
