# 002. Add Two Numbers - LeetCode
# https://leetcode.com/problems/add-two-numbers/description/

from helper.linked_list import ListNode, LinkedList, traversal

# Non Empty, reversed

# class Solution(object):
#     def addTwoNumbers(self,l1,l2):
#         def linkedlist_to_integer(l):
#             ret = 0
#             count = 0
#             head = l
#             while head:
#                 ret += head.val * ( 10 ** count )
#                 count += 1
#                 head = head.next
#             return ret
        
#         msum = linkedlist_to_integer(l1) + linkedlist_to_integer(l2)
        
#         ret = ListNode( msum % 10 )
#         msum //= 10
#         head = ret
#         while msum > 0:
#             head.next = ListNode( msum % 10 )
#             msum //= 10
#             head = head.next

#         return ret
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = l1
        b = l2
        c = 0
        while True:
            res = a.val + b.val + c
            c = 0
            if res > 9:
                c = 1
                res -= 10
            a.val = res
            if a.next is None:
                a.next = b.next
                break
            elif b.next is None:
                break
            a = a.next
            b = b.next
        while c > 0:
            if a.next is None:
                a.next = ListNode(1)
                c = 0
            elif a.next.val < 9:
                a.next.val += 1
                c = 0
            else:
                a.next.val = 0
                a = a.next
        return l1
        
ans = [
    ([1,2,3],[3,2,1],[4,4,4]),
    ([1,2,3],[1],[2,2,3]),
    ([1],[1,2,3],[2,2,3]),
    ([2,4,3],[5,6,4],[7,0,8]), #WA1
    ([5],[5],[0,1]), # WA2
    ([5],[5,1],[0,2]),
    ([1],[9,9],[0,0,1]), # WA3
    ([0],[0],[0]),
]

s = Solution()
for i in ans:
    ret = s.addTwoNumbers(LinkedList(i[0]).head,LinkedList(i[1]).head)
    print( "O" if traversal(ret) == i[2] else "X", traversal(ret), i[2] )