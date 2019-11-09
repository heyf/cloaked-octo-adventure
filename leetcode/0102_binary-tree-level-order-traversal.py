#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ret = []
        if root:
            ret.append([root.val])
            child = [root.left, root.right]
            while child:
                new_child = []
                current_layer = []
                for node in child:
                    if node:
                        current_layer.append(node.val)
                        if node.left:
                            new_child.append(node.left)
                        if node.right:
                            new_child.append(node.right)
                child = new_child
                if current_layer:
                    ret.append(current_layer)
        return ret

# @lc code=end
a = TreeNode(3)
a.left = TreeNode(9)
a.right = TreeNode(20)
a.right.left = TreeNode(15)
a.right.right = TreeNode(7)
s = Solution()
print(s.levelOrder(a))