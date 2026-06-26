# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0
    def diameterOfBinaryTreeHelper(self, root):
        if root is None:
            return 0

        left = self.diameterOfBinaryTreeHelper(root.left)
        right = self.diameterOfBinaryTreeHelper(root.right)
        self.diameter = max(self.diameter,left+right)
        return max(left, right)+1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:  
        self.diameterOfBinaryTreeHelper(root)
        return self.diameter
        