# 203. Remove Linked List Elements - LeetCode
# https://leetcode.com/problems/remove-linked-list-elements/description/

# Definition for singly-linked list.
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
        
    def traversal(self,head=-1):
        if head == -1:
            return self.lst
        ret = []
        while head:
            ret.append(head.val)
            head = head.next
        return ret

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val == val: # check head val
            head = head.next
        ret = head
        while head and head.next:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        return ret
            
        
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5

s = Solution()
ans = [
    ([],6,[]),
    ([6],6,[]),
    ([6,6,6,6,6,6],6,[]),
    ([1],6,[1]),
    ([6,1,2],6,[1,2]),
    ([6,1,2,6],6,[1,2]),
    ([1,2,6,3,4,5,6],6,[1,2,3,4,5]),
#     ([],[]),
]

for i in ans:
    l = LinkedList(i[0])
    r = l.traversal(s.removeElements(l.head,i[1]))
    print r, r == i[2]