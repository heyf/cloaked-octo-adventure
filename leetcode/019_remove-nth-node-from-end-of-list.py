'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        i = 0
        fast = head
        slow = head
        for i in xrange(n):
            fast = fast.next
        if fast is None:
            return head.next
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
        
def test():
    cases = list()
    cases.append( ([1], 1, []) )
    cases.append( ([1,2,3,4,5], 2, [1,2,3,5]) )# Given linked list: 1->2->3->4->5, and n = 2.
    cases.append( ([1,2], 2, [2]) ) # fast is None, so head removed
    
    def verify(case):
        s = Solution()
        head = gen_linked_list(case[0])
        print "in : ", pop_linked_list(head)
        ret = s.removeNthFromEnd(head, case[1])
        print "out: ", pop_linked_list(ret)
        print "ans: ", case[2]
        return  case[2] == pop_linked_list(ret)

    def gen_linked_list(lst):
        head = ListNode(lst[0])
        p = head
        for i in lst[1:]:
            p.next = ListNode(i)
            p = p.next
        return head
    
    def pop_linked_list(head):
        ret = []
        while head is not None:
            ret.append(head.val)
            head = head.next
        return ret
            
    result = filter(verify, cases)
    # print run()
    
    return len(result) == len(cases), len(result), len(cases)
    
test()