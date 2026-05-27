# Completed May, 26 2026 | 77 minutes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def ancestry(node):
            if not node:
                return

            left = ancestry(node.left)
            right = ancestry(node.right)

            if node.val == p.val:
                return p
            if node.val == q.val:
                return q

            if left and right:
                return node

            if left or right:
                if left:
                    return left
                else:
                    return right

        return ancestry(root)