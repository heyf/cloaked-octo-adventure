#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
    
    def __str__(self):
        return f"Node({self.val})"
# from collections import namedtuple
# Node = namedtuple("Node", ["val", "next", "random"])

# @lc code=start
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        pointer_mapping = {None:None}
        new_head = Node(-1, None, None)
        curr = head
        new_prev = new_head
        while curr:
            new_prev.next = Node(curr.val, None, None)
            pointer_mapping[curr] = new_prev.next
            new_prev = new_prev.next
            curr = curr.next
        curr = head
        new_curr = new_head.next
        while curr:
            new_curr.random = pointer_mapping[curr.random]
            curr = curr.next
            new_curr = new_curr.next
        return new_head.next

# @lc code=end
s = Solution()

head = Node(val=-1,next=None,random=None)
# head.random = head
new_head = s.copyRandomList(head)

while new_head:
    print(new_head)
    new_head = new_head.next