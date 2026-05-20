# Completed May, 19 2026 | 11 minutes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def scan(node: TreeNode) -> None:
            if not node:
                return

            node.left, node.right = node.right, node.left

            scan(node.left)
            scan(node.right)

        scan(root)
        return root

