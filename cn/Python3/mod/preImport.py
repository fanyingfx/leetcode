from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        l = []
        head = self
        while(head):
            l.append(str(head.val))
            head = head.next
        return '->'.join(l)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def init_List(l):
    h = ListNode(0)
    res = h
    for i in l:
        res.next = ListNode(i)
        res = res.next
    return h.next