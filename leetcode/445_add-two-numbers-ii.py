#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#

from helper.linked_list import ListNode, LinkedList, traversal

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next

        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        current_digit = ListNode(0)
        while s1 or s2:
            if s1:
                current_digit.val += s1.pop()
            if s2:
                current_digit.val += s2.pop()
            next_digit = ListNode(current_digit.val // 10)
            current_digit.val = current_digit.val % 10
            next_digit.next = current_digit
            if not s1 and not s2 and next_digit.val == 0:
                break
            current_digit = next_digit
        
        return current_digit

# @lc code=end
s = Solution()
l1 = LinkedList([7,2,4,3]).head
l2 = LinkedList([5,6,4]).head
head = s.addTwoNumbers(l1, l2)
print(traversal(head))
