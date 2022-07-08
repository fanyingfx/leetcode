# @algorithm @lc id=42 lang=python3 
# @title trapping-rain-water


from cn.Python3.mod.preImport import *
# @test([0,1,0,2,1,0,1,3,2,1,2,1])=6
# @test([4,2,0,3,2,5])=9
class Solution:
    def trap(self, height: List[int]) -> int:
        ''' 
        curr_vol=min(max_left,max_right)-curr_height
        max_left=max(perv_height,perv_max_left)
        max_right=max(next_height,perv_max_left)
        '''
        max_left=max_right=0
        left=0
        right=len(height)-1
        res=0
        while left<=right:
            if max_left<max_right:
                res+=max(0,max_left-height[left])
                max_left=max(max_left,height[left])
                left+=1
            else:
                res+=max(0,max_right-height[right])
                max_right=max(max_right,height[right])
                right-=1
        return res




