# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root):
        if root is None:
            return 0, True
        lh, lb=self.height(root.left)
        rh, rb=self.height(root.right)
        if lh-rh>1 or rh-lh>1:
            return 1+max(lh,rh),False
        elif lb and rb:
            return 1+max(lh,rh),True
        else:
            return 1+max(lh,rh),False
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        lh, lb = self.height(root.left)
        rh, rb=self.height(root.right)
        if lh-rh>1 or rh-lh>1:
            return False
        elif lb and rb:
            return True
        else:
            return False
        