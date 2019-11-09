#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# @lc code=start

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            ret = []
            ret += self.inorderTraversal(root.left)
            ret += [root.val]
            ret += self.inorderTraversal(root.right)
            return ret
        return []

# @lc code=end
a = TreeNode(1)
a.right = TreeNode(2)
a.right.left = TreeNode(3)
s = Solution()
print(s.inorderTraversal(a))
