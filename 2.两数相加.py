#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        promote_val=0
        dummy_head=ListNode()
        prev=dummy_head
        while l1 is not None or l2 is not None:
            curr=ListNode()
            curr_val=promote_val
            promote_val=0
            if l1 is not None: 
                curr_val+=l1.val
                l1=l1.next
            if l2 is not None: 
                curr_val+=l2.val
                l2=l2.next
            if curr_val>=10:
                promote_val=1
                curr_val-=10
            curr.val=curr_val
            prev.next=curr
            prev=curr
        if promote_val==1:
            curr=ListNode(val=1)
            prev.next=curr
        return dummy_head.next


            

# @lc code=end

