''' 83. Remove Duplicates from Sorted List - LeetCode
https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def traversal(node):
    while True :
        print node.val,
        node = node.next
        if node is None:
            print ""
            break
        
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        current_head = head
        while current_head.next is not None:
            if current_head.val == current_head.next.val:
                current_head.next = current_head.next.next
                continue
            current_head = current_head.next
        return head

a = ListNode(1)
p = a
for i in [1,2,2,3,3,3]:
    p.next = ListNode(i)
    p = p.next
    
traversal(a)

s = Solution()
traversal(s.deleteDuplicates(a))