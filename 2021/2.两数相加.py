#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        t1,t2=l1,l2
        carry=0
        head=ListNode()
        pre=head
        while t1 or t2:
            val:int = carry
            if t1:
                val += t1.val
                t1=t1.next
            if t2:
                val += t2.val
                t2=t2.next
            carry=0
            if val > 9:
                val=val-10
                carry=1
            curr = ListNode(val)
            pre.next=curr
            pre=curr
        if carry ==1:
            curr=ListNode(carry)
            pre.next=curr
        return head.next
        
        
# @lc code=end

