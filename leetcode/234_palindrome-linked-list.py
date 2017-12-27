# 234. Palindrome Linked List - LeetCode
# https://leetcode.com/problems/palindrome-linked-list/description/

from helper.linked_list import LinkedList, traversal

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def flip(head):
            if head is None or head.next is None:
                return head
            prev = None
            curr = head
            nxt = curr.next
            while nxt:
                curr.next = prev
                prev = curr
                curr = nxt
                nxt = nxt.next
            curr.next = prev
            return curr
        if head is None:
            return True
        if head.next is None:
            return True
        # find mid
        slow = head
        fast = head.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            # slow stop at middle
        # compare new_head and head
        a = head
        b = flip(slow.next)
#         while b.next: # WA1, [1,2], won't compare
        while b:
            if a.val != b.val:
                return False
            a = a.next
            b = b.next
        return True
        
ans = [
    ([],True),
    ([1],True),
    ([1,2],False),
    ([1,2,3],False),
    ([1,2,1],True),
    ([1,2,3,3,2,1],True),
    ([1,2,3,4,5],False),
    ([1,2,3,4,3,2,1],True),
    ([2,2,2,2],True),
    (range(10),False),
]

s = Solution()
for i in ans:
    l = LinkedList(i[0])
    r = s.isPalindrome(l.head)
    print r, "O" if r == i[1] else "X"