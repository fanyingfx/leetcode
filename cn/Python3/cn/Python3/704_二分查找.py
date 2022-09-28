# @algorithm @lc id=792 lang=python3 
# @title binary-search


from cn.Python3.mod.preImport import *
# @test([-1,0,3,5,9,12],9)=4
# @test([-1,0,3,5,9,12],2)=-1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>target:
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
        return -1

       