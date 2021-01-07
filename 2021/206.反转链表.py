#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        curr = head.next
        pre=head
        pre.next =None
        while curr is not None:
            next = curr.next
            curr.next = pre
            pre=curr
            curr= next
            
        return pre


# @lc code=end

