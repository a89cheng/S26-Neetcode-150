# Completed May, 19 2026 | 9.5 minutes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def diver(node, deep=0):
            if not node:
                return deep

            left = diver(node.left, deep + 1)
            right = diver(node.right, deep + 1)
            return max(left, right)

        return diver(root)

