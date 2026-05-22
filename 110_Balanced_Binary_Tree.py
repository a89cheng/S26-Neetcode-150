# Completed May, 21 2026 | 21.5 minutes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def searcher(node, failed):
            if not node:
                return failed, 0

            failed, left_h = searcher(node.left, failed)
            left_h += 1
            failed, right_h = searcher(node.right, failed)
            right_h += 1

            if abs(left_h - right_h) <= 1:
                return failed, max(left_h, right_h)
            else:
                return True, max(left_h, right_h)

        return not searcher(root, False)[0]

