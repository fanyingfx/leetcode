#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#

# @lc code=start
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        m,n = len(nums1),len(nums2)
        if m > n:
            nums1,nums2 ,m,n = nums2,nums1,n,m
        if n == 0:
            raise ValueError

        imin,imax,half_len=0,m,(m+n+1)//2

        while imin <= imax:
            i = (imin+imax)//2
            j = half_len -i

            if i< m and nums2[j-1] > nums1[i]: # i 太小 要加大
                imin = i +1
            elif  i> 0 and nums2[j] < nums1[i-1]: # i 太大 要 减小
                imax = i - 1

            else: # nums2[j-1] <= nums1[i] and nums1[i-1]<=nums2[j]
                # i is perfect
                if i == 0: max_of_left=nums2[j-1]
                elif j == 0: max_of_left=nums1[i-1]
                else: max_of_left=max(nums1[i-1],nums2[j-1])
                print(f'l:{max_of_left}')

                if (m+n) % 2 == 1:
                    return max_of_left
                
                if i == m: min_of_right=nums2[j]
                elif j==n: min_of_right=nums1[i]
                else: min_of_right=min(nums1[i],nums2[j])
                print(f'l:{max_of_left},r:{min_of_right}')

                return (max_of_left+min_of_right)/2

sln = Solution()

nums1 = [1,2]
nums2 = [3,4]

print(sln.findMedianSortedArrays(nums1,nums2))









        
# @lc code=end

