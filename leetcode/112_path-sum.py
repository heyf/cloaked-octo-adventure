# 112. Path Sum - LeetCode
# https://leetcode.com/problems/path-sum/description/

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def has_sum_with_parent( self, root, current_sum, target_sum ):
        if root is None:
            return False
        current_sum += root.val
        if root.left is None and root.right is None:
            if current_sum == target_sum:
                return True
        # Cause of WA1
#         if current_sum > target_sum:
#             return False 
        return ( self.has_sum_with_parent( root.left, current_sum, target_sum ) 
            or self.has_sum_with_parent( root.right, current_sum, target_sum ) )

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.has_sum_with_parent( root, 0, sum )
        
        
s = Solution()
tn = TreeNode(1)
tn.left = TreeNode(2)
tn.right = TreeNode(3)
tn.left.left = TreeNode(4)
tn.left.right = TreeNode(5)
tn.left.left.left = TreeNode(6)

print s.hasPathSum(tn,13)
print s.hasPathSum(tn,12)

# WA1, [-2,null,-3]
tn = TreeNode(-2)
tn.right = TreeNode(-3)
print s.hasPathSum(tn,-5)