#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (36.46%)
# Likes:    2270
# Dislikes: 0
# Total Accepted:    155.1K
# Total Submissions: 418.5K
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
# 
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
# 
# 你可以假设 nums1 和 nums2 不会同时为空。
# 
# 示例 1:
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# 则中位数是 2.0
# 
# 
# 示例 2:
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# 则中位数是 (2 + 3)/2 = 2.5
# 
# 
#

# @lc code=start
# from Utils import *
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n = len(nums1),len(nums2)
        if m > n:
            m,n,nums1,nums2 = n,m,nums2,nums1
        imin,imax = 0,m
        half_len = (m+n+1)//2

        while imin <= imax:
            i = (imin + imax +1)//2
            j = half_len - i
            if  i> 0 and nums2[j] < nums1[i-1]:
                imax = i-1
            elif i<m and nums1[i] < nums2[j-1]:
                imin = i+1

            else:
                # B[j] > = A[i-1] and A[i] >= B[j-1]
                if i == 0: max_left = nums2[j-1]
                elif j == 0: max_left = nums1[i-1]
                else: max_left = max(nums1[i-1],nums2[j-1])

                # 奇数个 则左边有 k+1 个文件，所以返回左边最大的值就行
                if (m+n) % 2 == 1:
                    return max_left
                else:
                    if i == m: min_right = nums2[j]
                    elif j==n: min_right = nums1[i]
                    else:
                        min_right = min(nums1[i],nums2[j])
                    print(max_left,min_right)
                    return (max_left+min_right)/2
                
                    
sln = Solution()

nums1 = [100001]
nums2 =  [100000]
print(sln.findMedianSortedArrays(nums1,nums2))
                



# @lc code=end

