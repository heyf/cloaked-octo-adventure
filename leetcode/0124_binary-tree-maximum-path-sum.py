#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# @lc code=start
class Solution:
    global_max = None
    def update_global_max(self, val):
        if self.global_max:
            self.global_max = max(self.global_max, val)
        else:
            self.global_max = val

    def helper(self, root):
        # return maxsum with single leaf, update global max for current root
        if root:
            self.update_global_max(root.val)
            left = self.helper(root.left)
            right = self.helper(root.right)
            ret = max( root.val + left, root.val + right )
            ret = max( root.val, ret)
            self.update_global_max(ret)
            self.update_global_max(root.val + left + right)
            return ret
        return 0

    def maxPathSum(self, root: TreeNode) -> int:
        self.helper(root)
        return self.global_max if self.global_max else 0

# @lc code=end
from helper.tree import create_tree_by_list
null = None
a = create_tree_by_list([-10,9,20,null,null,15,7])
s = Solution()
print(s.maxPathSum(a))