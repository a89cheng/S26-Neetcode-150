# Completed May, 20 2026 | 46.5 minutes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diver(node):
            if not node:
                return 0, 0

            l_height, l_diameter = diver(node.left)
            r_height, r_diameter = diver(node.right)

            max_height = max(l_height, r_height) + 1
            diameter_through_node = r_height + l_height

            return max_height, max(diameter_through_node, l_diameter, r_diameter)

        return diver(root)[1]