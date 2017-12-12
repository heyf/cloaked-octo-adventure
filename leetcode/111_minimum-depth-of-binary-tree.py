# 111. Minimum Depth of Binary Tree - LeetCode
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        if root.left is None:
            return self.minDepth(root.right) + 1
        if root.right is None:
            return self.minDepth(root.left) + 1
        return min( self.minDepth(root.left), self.minDepth(root.right) ) + 1
    
s = Solution()
tn = TreeNode(1)
tn.left = TreeNode(2)
tn.right = TreeNode(3)
tn.left.left = TreeNode(4)
tn.left.right = TreeNode(5)
tn.left.left.left = TreeNode(6)

print s.minDepth(tn)