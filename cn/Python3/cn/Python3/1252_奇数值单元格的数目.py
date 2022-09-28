# @algorithm @lc id=1378 lang=python3 
# @title cells-with-odd-values-in-a-matrix


from cn.Python3.mod.preImport import *
# @test(2,3,[[0,1],[1,1]])=6
# @test(2,2,[[1,1],[0,0]])=0
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        martix=[[0]*n for _ in range(m)]
        count=0
        for idx in indices:
            x,y=idx
            for i in range(n):
                martix[x][i]+=1
            for j in range(m):
                martix[j][y]+=1
        for i in range(m):
            for j in range(n):
                if martix[i][j] %2 ==1:
                    count+=1
        
        return count
            
