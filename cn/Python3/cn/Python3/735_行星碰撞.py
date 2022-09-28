# @algorithm @lc id=735 lang=python3 
# @title asteroid-collision


from cn.Python3.mod.preImport import *
# @test([5,10,-5])=[5,10]
# @test([8,-8])=[]
# @test([10,2,-5])=[10]
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        alive=True
        for aster in asteroids:
            alive=True
            while alive and stack and stack[-1]>0 and aster<0:
                alive=stack[-1]<-aster
                if stack[-1]<=-aster:
                    stack.pop()
            if alive:
                stack.append(aster)
        
        return stack
                