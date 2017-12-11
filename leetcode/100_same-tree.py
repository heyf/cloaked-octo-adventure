# 100. Same Tree - LeetCode
# https://leetcode.com/problems/same-tree/description/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
def pre_order_traversal(tn):
    res = [tn.val]
    if tn.left is None and tn.right is None:
        return res
    if tn.left != None:
        res += pre_order_traversal(tn.left)
    else:
        res += [None]
    if tn.right != None:
        res += pre_order_traversal(tn.right)
    else:
        res += [None]
    return res

t = TreeNode(1)
# t.left = TreeNode(2)
t.right = TreeNode(3)

pre_order_traversal(t)
    
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:
            return False
        
s = Solution()

p = TreeNode(1)
p.right = TreeNode(3)

q = TreeNode(1)
q.right = TreeNode(3)

s.isSameTree(p,q)