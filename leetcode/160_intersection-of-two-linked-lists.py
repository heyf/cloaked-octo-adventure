# 160. Intersection of Two Linked Lists - LeetCode
# https://leetcode.com/problems/intersection-of-two-linked-lists/description/

# Your code should preferably run in O(n) time and use only O(1) memory.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len_a = 0
        len_b = 0
        pa = headA
        pb = headB
        while True:
            if pa is None:
                break
            pa = pa.next
            len_a += 1
        while True:
            if pb is None:
                break
            pb = pb.next
            len_b += 1
        pa = headA
        pb = headB
        delta = len_a - len_b
        while delta != 0:
            if delta > 0: # len_a > len_b
                pa = pa.next
                delta -= 1
            else:
                pb = pb.next
                delta += 1
        while pa:
            if pa == pb:
                return pa
            else:
                pa = pa.next
                pb = pb.next
        return None

s = Solution()

c1 = ListNode("c1")
c1.next = ListNode("c2")
c1.next.next = ListNode("c3")
a1 = ListNode("a1")
a1.next = ListNode("a2")
a1.next.next = c1
b1 = None
print s.getIntersectionNode(a1,b1) # None
b1 = ListNode("b1")
print s.getIntersectionNode(a1,b1) # None
b2 = ListNode("b2")
b1.next = b2
b2.next = c1
print s.getIntersectionNode(a1,b1) # c1