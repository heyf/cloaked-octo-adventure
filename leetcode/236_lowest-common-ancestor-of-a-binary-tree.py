#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

from helper.tree import TreeNode, create_tree_by_list, tree_traversal

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or p is root or q is root:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right

# @lc code=end
s = Solution()
null = None
# Example 1:
root = [3,5,1,6,2,0,8,null,null,7,4]
# p = 5
# q = 1
# Output: 3
# Example 2:
# root = [3,5,1,6,2,0,8,null,null,7,4]
p = 5
q = 4
# Output: 5
# Code
root = create_tree_by_list(root)
node_list = tree_traversal(root, value=False)
# print([node.val if node else None for node in node_list])
p, q = [ node_list[idx] for idx in [p, q] ]
ret = s.lowestCommonAncestor(root, p, q)
print(ret.val)