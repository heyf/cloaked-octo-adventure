def traversal(head):
    # Todo: loop detect
    ret = []
    while head:
        ret.append(head.val)
        head = head.next
    return ret

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList(object):
    def __init__(self, lst):
        self.lst = lst
        if len(lst) == 0:
            self.head = None
            return
        self.head = ListNode(lst[0])
        p = self.head
        for i in lst[1:]:
            p.next = ListNode(i)
            p = p.next
    
    def display(self):
        return self.lst