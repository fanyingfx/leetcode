# @algorithm @lc id=905 lang=python3 
# @title length-of-longest-fibonacci-subsequence


from cn.Python3.mod.preImport import *
# @test([1,2,3,4,5,6,7,8])=5
# @test([1,3,7,11,12,14,18])=3
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        length=len(arr)
        max_val=arr[-1]
        if length<3:
            return 0
        fib=[]
        max_len=0
        d={}
        for i in range(length):
            d[arr[i]]=i
        for i in range(length):
            for j in range(i+1,length):
                curr_val=arr[i]+arr[j]
                last_val=arr[j]
                curr_len=2
                while curr_val<=max_val:
                    if curr_val in d:
                        curr_len+=1
                        max_len=max(curr_len,max_len)
                        t=curr_val
                        curr_val=last_val+curr_val
                        last_val=t
                    else:
                        break
        return max_len
                