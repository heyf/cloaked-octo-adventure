#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# @lc code=start
# Definition for a binary tree node.

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        current_layer = [root]
        next_layer = []
        while current_layer:
            bottom_left = current_layer[0]
            for root in current_layer:
                if root.left:
                    next_layer.append(root.left)
                if root.right:
                    next_layer.append(root.right)
            current_layer = next_layer
            next_layer = []
        return bottom_left.val

# @lc code=end
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.right.left.left = TreeNode(7)
s = Solution()
ret = s.findBottomLeftValue(root)
print(ret.val)
