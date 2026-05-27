# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSumHelper(self, root, sum_t, targetSum):
        if root is None:
            return False
        if root.left is None and root.right is None:
            if root.val + sum_t == targetSum:
                return True
            else:
                return False
            
        left_sum = self.hasPathSumHelper(root.left, sum_t+root.val, targetSum)
        right_sum = self.hasPathSumHelper(root.right, sum_t+root.val, targetSum)

        if left_sum or right_sum:
            return True
        else:
            return False

        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.hasPathSumHelper(root, 0, targetSum)

        