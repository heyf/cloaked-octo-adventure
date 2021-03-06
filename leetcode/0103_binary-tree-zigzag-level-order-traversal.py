#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ret = []
        child = [root]
        flag = True
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
                if flag:
                    ret.append(current_layer)
                else:
                    ret.append(current_layer[::-1])
            flag = not flag
        return ret

# @lc code=end
b = [1,2,3,4,None,None,5] # WA1
a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.left.left = TreeNode(4)
a.right.right = TreeNode(5)
s = Solution()
print(s.zigzagLevelOrder(a))
