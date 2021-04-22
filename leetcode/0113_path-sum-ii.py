from typing import List

'''
Runtime: 92 ms, faster than 5.74% of Python3 online submissions for Path Sum II.
Memory Usage: 15.6 MB, less than 63.45% of Python3 online submissions for Path Sum II.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:

        if not root:
            return []

        ret = []
        stack = []

        def helper(current_root, current_sum):
            if not current_root:
                return
            
            stack.append(current_root.val)
            
            if current_root.val == current_sum and not current_root.left and not current_root.right:
                ret.append(stack.copy())
            
            helper(current_root.left, current_sum-current_root.val)
            helper(current_root.right, current_sum-current_root.val)

            stack.pop(-1)
        
        helper(root, sum)
        
        return ret

s = Solution()
tn = TreeNode(1)
tn.left = TreeNode(2)
tn.right = TreeNode(3)
tn.left.left = TreeNode(4)
tn.left.right = TreeNode(5)
tn.left.left.left = TreeNode(6)

print(s.pathSum(tn,1))