# 141. Linked List Cycle - LeetCode
# https://leetcode.com/problems/linked-list-cycle/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# TLE:
# class Solution(object):
#     def hasCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         ptr = head
#         total_call = 0
#         while True:
#             if ptr is None:
#                 break
#             call_count = 0
#             working_ptr = head
#             while call_count < total_call:
#                 if working_ptr == ptr:
#                     return True
#                 else:
#                     call_count += 1
#                     working_ptr = working_ptr.next
#             ptr = ptr.next
#             total_call += 1
#         return False

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        slow = head
        fast = head.next
        while True:
            if slow == fast:
                return True
            if fast.next is None or fast.next.next is None or slow.next is None:
                return False
            slow = slow.next
            fast = fast.next.next

s = Solution()
l = None
print(s.hasCycle(l))
l = ListNode(0)
print(s.hasCycle(l))
l.next = ListNode(1)
l.next.next = ListNode(2)
l.next.next.next = ListNode(3)
print(s.hasCycle(l))
l.next.next.next.next = l.next
print(s.hasCycle(l))