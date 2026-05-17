# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            if root is None:
                return [0,0]

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            withroot = root.val + leftMax[1] + rightMax[1]
            withoutroot = max(leftMax) + max(rightMax)

            return [withroot, withoutroot]

        return max(dfs(root))
        