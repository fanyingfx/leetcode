# @algorithm @lc id=21 lang=python3 
# @title merge-two-sorted-lists


from typing import Optional
from cn.Python3.mod.preImport import *
# @test([1,2,4],[1,3,4])=[1,1,2,3,4,4]
# @test([],[])=[]
# @test([],[0])=[0]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if list1.val>list2.val:
            list1,list2=list2,list1
        h1=list1
        print(list1)
        print(list2)
                    
        while list1 and list2:
            if list1.val > list2.val:
                list1,list2=list2,list1
            while list1.next and list1.next.val<=list2.val:
                list1=list1.next
            l1=list1.next
            list1.next=list2
            list1=l1
        
        return h1
            

sln=Solution()
# sln.mergeTwoLists(init_List([1,4,5,6]),init_List([2,3,7,8]))
# r=sln.mergeTwoLists(init_List([1,2,4]),init_List([1,3,4]))
# print(r)


