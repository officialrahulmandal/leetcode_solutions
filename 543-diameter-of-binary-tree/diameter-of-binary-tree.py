# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTreeHelper(self, root):
        if root is None:
            return 0, 0
        leftBranch, lDiameter= self.diameterOfBinaryTreeHelper(root.left)
        rightBranch, rDiameter= self.diameterOfBinaryTreeHelper(root.right)
        longest_branch =max(leftBranch, rightBranch)
        diameter=max(leftBranch+rightBranch+1, lDiameter, rDiameter)
        return longest_branch+1, diameter



    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        longestBranch, diameter= self.diameterOfBinaryTreeHelper(root)
        return diameter-1
        