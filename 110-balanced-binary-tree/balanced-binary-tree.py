# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root):
        if root is None:
            return 0
        lh=self.height(root.left)
        rh=self.height(root.right)
        return 1+max(lh,rh)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        lh = self.height(root.left)
        rh=self.height(root.right)
        if lh-rh>1 or rh-lh>1:
            return False
        lb=self.isBalanced(root.left)
        rb=self.isBalanced(root.right)
        if lb and rb:
            return True
        else:
            return False
        