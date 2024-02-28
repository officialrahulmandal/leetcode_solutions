# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValueHelper(self, root):
        if root.left is None and root.right is None:
            return 0, root.val
        
        left_d = None
        right_d = None
        left_v = 0
        right_v = 0
        if root.left is not None:
            left_d, left_v = self.findBottomLeftValueHelper(root.left)
        if root.right is not None:
            right_d, right_v = self.findBottomLeftValueHelper(root.right)

        if left_d is None:
            value=right_v
            diameter=right_d
        elif right_d is None:
            value = left_v
            diameter=left_d
        elif left_d<right_d:
            value=right_v
            diameter=right_d
        else:
            value = left_v
            diameter=left_d

        return diameter+1, value

        


    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.findBottomLeftValueHelper(root)[1]

        