#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# https://leetcode-cn.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (36.28%)
# Likes:    4261
# Dislikes: 0
# Total Accepted:    403.9K
# Total Submissions: 1.1M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 
# 示例：
# 
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
# 
# 
#

# @lc code=start
# Definition for singly-linked list.


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = ListNode(0)
        res= head
        while l1 is not None or l2 is not None:

            x1 = l1.val if l1 is not None else 0
            x2 = l2.val if l2 is not None else 0
            v = x1 + x2+carry
            carry = 0
            if v > 9:
                carry = 1
                v -= 10

            res.next = ListNode(v)
            res = res.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        
        if carry ==1:
            res.next = ListNode(1)

        return head.next

# @lc code=end

