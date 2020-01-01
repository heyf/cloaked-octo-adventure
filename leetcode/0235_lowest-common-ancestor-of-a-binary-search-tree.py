#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

from helper.tree import TreeNode, create_tree_by_list

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > max(p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

# @lc code=end
null = None
s = Solution()
# Example 1:
# root = [6,2,8,0,4,7,9,null,null,3,5]
# p, q = 2, 8
# Example 2:
root = [6,2,8,0,4,7,9,null,null,3,5]
p, q = 2, 4
# Code:
root, pq = create_tree_by_list(root, node_indexes=[p, q])
p, q = pq
ret = s.lowestCommonAncestor(root, p, q)
print(ret.val)