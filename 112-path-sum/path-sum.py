# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSumHelper(self, node,remaining):
        if node is None:
            return False

        if node.left is None and node.right is None:
            return remaining==node.val

        left = self.hasPathSumHelper(node.left, remaining - node.val)
        right = self.hasPathSumHelper(node.right, remaining - node.val)

        return left or right

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        return self.hasPathSumHelper(root,targetSum)
        
        