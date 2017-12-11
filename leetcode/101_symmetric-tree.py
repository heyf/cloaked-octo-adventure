# 101. Symmetric Tree - LeetCode
# https://leetcode.com/problems/symmetric-tree/description/
# Bonus points if you could solve it both recursively and iteratively.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        if root.left is None or root.right is None:
            return False
        if root.left.val == root.right.val:
            new_tree_left = TreeNode(None)
            new_tree_left.left = root.left.left
            new_tree_left.right = root.right.right
            new_tree_right = TreeNode(None)
            new_tree_right.left = root.left.right
            new_tree_right.right = root.right.left
            return self.isSymmetric(new_tree_left) and self.isSymmetric(new_tree_right)
        else:
            return False

s = Solution()

p = TreeNode(1)
p.left = TreeNode(3)
p.right = TreeNode(3)
p.left.left = TreeNode(5)
# p.right.right = TreeNode(5)

print s.isSymmetric(p)