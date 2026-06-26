from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        results = []
        queue = deque()
        queue.append(root)
        while queue:
            n = len(queue)
            small_output = []
            for _ in range(n):
                value = queue.popleft()
                if value.left:
                    queue.append(value.left)
                if value.right:
                    queue.append(value.right)
                small_output.append(value.val)
            results.append(small_output)
        return results


        
        