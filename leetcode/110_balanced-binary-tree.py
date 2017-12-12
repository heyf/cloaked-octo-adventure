# 110. Balanced Binary Tree - LeetCode
# https://leetcode.com/problems/balanced-binary-tree/description/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def get_depth(self, root):
        if root is None:
            return 0
        ld = self.get_depth(root.left)
        if ld == -1:
            return -1
        rd = self.get_depth(root.right)
        if rd == -1:
            return -1
        delta = ld - rd
        if delta > 1 or delta < -1:
            return -1
        return max(ld,rd) + 1
         
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if self.get_depth(root) > -1:
            return True
        return False
    
s = Solution()
tn = TreeNode(1)
tn.left = TreeNode(2)
tn.left.right = TreeNode(3)
s.isBalanced(tn)
# s.get_depth(tn.left)