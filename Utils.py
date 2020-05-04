class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        l = []
        head = self
        while(head):
            l.append(str(head.val))
            head = head.next
        return '->'.join(l)

def init_List(l):
    h = ListNode(0)
    res = h
    for i in l:
        res.next = ListNode(i)
        res = res.next
    return h.next
