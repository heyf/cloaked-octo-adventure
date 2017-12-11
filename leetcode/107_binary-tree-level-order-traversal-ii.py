# 107. Binary Tree Level Order Traversal II - LeetCode
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):        
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        else: 
            res = []
            next_level = [root]
            while len(next_level) > 0:
                current_level = next_level
                current_output = []
                next_level = []
                for i in current_level:
                    if i:
                        current_output.append(i.val)
                        next_level += [ i.left, i.right ]
                if len(current_output) > 0:
                    res.insert(0,current_output)
            return res

tn = TreeNode(1)
tn.left = TreeNode(2)
tn.right = TreeNode(3)
tn.left.left = TreeNode(4)

s = Solution()
s.levelOrderBottom(tn)