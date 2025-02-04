# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

class Solution:
    def pathSumHelper(self, root: Optional[TreeNode], targetSum: int, current_path: List[int]) -> int:
        if root is None:
            return 0
        
        # Add the current node's value to the path
        current_path.append(root.val)
        
        count = 0
        path_sum = 0
        
        # Check if any sub-path sums up to targetSum
        for value in reversed(current_path):
            path_sum += value
            if path_sum == targetSum:
                count += 1
        
        # Recur for left and right subtrees
        count += self.pathSumHelper(root.left, targetSum, current_path)
        count += self.pathSumHelper(root.right, targetSum, current_path)
        
        # Backtrack: remove the current node's value from the path
        current_path.pop()
        
        return count

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return self.pathSumHelper(root, targetSum, [])
