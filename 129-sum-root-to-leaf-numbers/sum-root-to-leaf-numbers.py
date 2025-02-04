# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbersHelper(self, root,carryForward):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return int(carryForward+str(root.val))
        sum_L = self.sumNumbersHelper(root.left,carryForward+str(root.val))
        sum_R = self.sumNumbersHelper(root.right,carryForward+str(root.val))
        return sum_L+sum_R


    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return
        return self.sumNumbersHelper(root,'')


        