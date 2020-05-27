#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# from Utils import ListNode,init_List

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        first_node = head
        second_node = head

        while n > 0:
            second_node=second_node.next
            n-=1
        if second_node is None:
            return first_node.next
        while second_node.next is not None:
            first_node = first_node.next
            second_node = second_node.next
        first_node.next = first_node.next.next
        


        return head

# sln = Solution()

# l = init_List([1,2,3,4,5])
# print(sln.removeNthFromEnd(l,5))

# @lc code=end

