# @algorithm @lc id=541 lang=python3 
# @title reverse-string-ii


from cn.Python3.mod.preImport import *
# @test("abcdefg",2)="bacdfeg"
# @test("abcd",2)="bacd"
# @test("ab",2)="ba"
# @test("a", 2)="a"
# @test("abcdefg", 8)="gfedcba"
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        stack=[]
        res=[]
        i=1
        for char in s:
            if i<k:
                stack.append(char)
                i+=1
            elif i==k:
                stack.append(char)
                i+=1
                res+=stack[::-1]
                stack.clear()
            elif k<i<k*2:
                res.append(char)
                i+=1
            else:
                i=1
                res.append(char)
        if stack:
            res+=stack[::-1]
        return ''.join(res)
                

