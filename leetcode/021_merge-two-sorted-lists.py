# 21. Merge Two Sorted Lists - LeetCode
# https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
a = ListNode(0)
p = a
for i in [1,3,4,5,7,10]:
    p.next = ListNode(i)
    p = p.next
    
b = ListNode(-1)
p = b
for i in [2,8,15]:
    p.next = ListNode(i)
    p = p.next

# Need to implement a linked list first
        
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val >= l2.val:
            i = ListNode(l2.val)
            i.next = self.mergeTwoLists( l1,l2.next )
            return i
        if l1.val < l2.val:
            i = ListNode(l1.val)
            i.next = self.mergeTwoLists( l1.next,l2 )
            return i

s = Solution()

def traversal(node):
    while True :
        print node.val,
        node = node.next
        if node is None:
            print "<"
            break

traversal(a)
traversal(b)
traversal(s.mergeTwoLists(a,b))