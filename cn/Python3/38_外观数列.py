# @algorithm @lc id=38 lang=python3 
# @title count-and-say


from cn.Python3.mod.preImport import *
# @test(1)="1"
# @test(4)="1211"
# @test(5)="111221"
class Solution:
    def countAndSay(self, n: int) -> str:
        l=[None]*(n)
        l[0]="1"
        for i in range(1,n):
            pre=l[i-1]
            pre_c=pre[0]
            count=0
            r=[]
            for v in pre:
                if v==pre_c:
                    count+=1
                else:
                    r.append(f'{count}{pre_c}')
                    pre_c=v
                    count=1
            r.append(f'{count}{pre_c}')
            l[i]=''.join(r)

        
        return l[n-1]
        
