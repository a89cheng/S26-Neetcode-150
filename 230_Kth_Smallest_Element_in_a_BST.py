# Completed May, 28 2026 | 27 minutes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def searcher(node):
            if not node:
                return False

            left = searcher(node.left)
            if len(results) < k:
                results.append(node.val)
            right = searcher(node.right)

            return True

        results = []
        searcher(root)
        return results[-1]

