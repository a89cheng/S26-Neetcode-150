# Completed May, 27 2026 | 39 minutes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def verifier(node, lower, upper):
            if not node:
                return True

            left = verifier(node.left, lower, node.val)
            right = verifier(node.right, node.val, upper)

            if left and right:
                if lower < node.val < upper:
                    return True
            else:
                return False

        return verifier(root, float("-inf"), float("inf"))