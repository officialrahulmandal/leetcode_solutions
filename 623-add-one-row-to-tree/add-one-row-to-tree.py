# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def addOneRowHelper(self, root: Optional[TreeNode], val: int, depth: int, current_depth: int):
        if root is None:
            return
        
        if current_depth == depth - 1:
            # Add a new node with value `val` as the parent of the current left child
            new_left = TreeNode(val)
            new_left.left = root.left
            root.left = new_left
            
            # Add a new node with value `val` as the parent of the current right child
            new_right = TreeNode(val)
            new_right.right = root.right
            root.right = new_right
            
        else:
            # Recur for left and right subtrees
            self.addOneRowHelper(root.left, val, depth, current_depth + 1)
            self.addOneRowHelper(root.right, val, depth, current_depth + 1)

    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            # If depth is 1, create a new root
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        
        # Start recursion
        self.addOneRowHelper(root, val, depth, 1)
        return root
