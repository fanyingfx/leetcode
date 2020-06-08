#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# from Utils import ListNode,init_List 

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        new_list=dummy
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                new_list.next = l1
                l1=l1.next
            else:
                new_list.next =l2
                l2= l2.next
            new_list = new_list.next
        # print('new_list',new_list)
        if l1:
            rest =l1
        else:
            rest =l2
        # print('rest',rest)
        while rest:
            new_list.next=rest
            new_list=new_list.next
            rest=rest.next
        return dummy.next

# sln = Solution()
# print(sln.mergeTwoLists(init_List([]),init_List([])))
# @lc code=end
# print(init_List([1,2,3,4]))

