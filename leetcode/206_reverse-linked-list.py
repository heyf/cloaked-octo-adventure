# 206. Reverse Linked List - LeetCode
# https://leetcode.com/problems/reverse-linked-list/description/

from helper.linked_list import ListNode, LinkedList, traversal

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head
        prev = None
        curr = head
        nxt = curr.next
        while nxt:
            curr.next = prev
            prev = curr
            curr = nxt
            nxt = curr.next
        curr.next = prev
        return curr
        
ans = [
    (range(100),range(99,-1,-1))
]

s = Solution()
for i in ans:
    a = LinkedList(i[0]).head
    r = traversal(s.reverseList(a))
    print r == i[1]