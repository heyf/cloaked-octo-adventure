# 101. Symmetric Tree - LeetCode
# https://leetcode.com/problems/symmetric-tree/description/

# iteratively trial
# TLE

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        next_level = [root]
        value_count = 1
        while len(next_level) > 0:
            if value_count == 0:
                return True
            current_level = next_level
            current_output = []
            next_level = []
            value_count = 0
            for i in current_level:
                if i:
                    value_count = 1
                    current_output.append(i.val)
                    next_level += [ i.left, i.right ]
                else:
                    current_output.append( None )
                    next_level += [ None, None ]
            x = 0
            while x < len(current_output):
                if current_output[x] != current_output[len(current_output)-x-1]:
                    return False
                x += 1

s = Solution()

p = TreeNode(1)
p.left = TreeNode(3)
p.right = TreeNode(3)
p.left.left = TreeNode(5)
# p.right.right = TreeNode(5)

print s.isSymmetric(p)