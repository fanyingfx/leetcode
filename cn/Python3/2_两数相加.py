# @algorithm @lc id=2 lang=python3 
# @title add-two-numbers

from cn.Python3.mod.preImport import *
# @test([2,4,3],[5,6,4])=[7,0,8]
# @test([0],[0])=[0

# @test([9,9,9,9,9,9,9],[9,9,9,9])=[8,9,9,9,0,0,0,1]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: