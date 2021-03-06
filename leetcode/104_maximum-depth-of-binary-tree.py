# 104. Maximum Depth of Binary Tree - LeetCode
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            return 1 + max( self.maxDepth(root.left), self.maxDepth(root.right) ) 
        
tn = TreeNode(1)
tn.left = TreeNode(2)
tn.left.left = TreeNode(3)

s = Solution()
s.maxDepth(tn)