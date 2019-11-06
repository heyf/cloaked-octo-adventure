#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def append_node(node, value):
    node.next = ListNode(value)
    return node.next

def traversal(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# @lc code=start
# Definition for singly-linked list.

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        ret = ListNode(-1)
        ret.next = head
        prev = ret
        while prev.next and prev.next.next:
            p, q = prev.next, prev.next.next
            prev.next = q
            p.next, q.next = q.next, p
            prev = p
        return ret.next

# @lc code=end
head = None
# head = ListNode(1)
# node = append_node(head, 2)
# node = append_node(node, 3)
# node = append_node(node, 4)
# node = append_node(node, 5)
print(traversal(head))
s = Solution()
head = s.swapPairs(head)
print(traversal(head))